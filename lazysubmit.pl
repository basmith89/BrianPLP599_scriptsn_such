#!/usr/bin/env perl

use warnings;
use strict;
use Getopt::Long;
#Written by August Woerner. This script attempts to
# create a bash submit script for PBS systems.

# constants; these are specific to the UAs HPC system
my $ramPerProc = 1866;
my $MAXCPUS = 12;
my $MAX_DEFAULT_RAM = 23500;
# arguments to hpc
my $numProcs=1;
my $ram = 0;
my $help=0;
my $clusterOnly=0;
my $htcOnly=0;
my $smpOnly=0;
my $queue = 'windfall';
my $name = '';
my $wallTime = 100;
my $group = '';
my $email='';
my $join=0;
my @modules = ();

GetOptions('p=i' => \$numProcs,
	   'm=i' => \$ram,
	   'e=s' => \$email,
	   'n=s' => \$name,
	   'g=s' => \$group,
	   'm=s' => \@modules,
	   'c' => \$clusterOnly,
	   'h' => \$htcOnly,
	   's' => \$smpOnly,
	   'q=s' => \$queue,
	   'w=i' => \$wallTime,
	   'j' => \$join,
	   'help' => \$help);



if ($help || ! @ARGV) {
    die "Usage:\n$0 commandYou'dLikeToRunOnTheHPC (you should probably surround that command with double quotes)\n" ,
    "\nOptions\n\t\n\t-g group (the group you'd like to submit the job under)\n\t-w walltime (the amount of time needed, according to the clock on the wall, in hours)\n\t-n jobName\b\n\t-q queue (windfall,standard or high_priority)\n\t-p numProcs (the number of processors you need)\n\t-m megsOfMemory (the number of megabytes of memory required)\n\t-c (runs jobs on the cluster)\n\t-h (runs jobs on the hpc)\n\t-s (runs jobs on the smp)\n\t-e emailAccount (this spams your email account)\n\t-j (this joins the standard output/error files)\n\t-m moduleName (this adds 'module load moduleName' to your script. It can be specified multiple times)\n\n";
}

if ($numProcs < 1 || ($numProcs > $MAXCPUS && ! $smpOnly)) {
    die "The number of processors you asked for makes no sense! For the htc/cluster, pick a number between 1 and 12\n";
}

# you can specify either how much memory you want, or
# how many processors (as one specifies the other)
if ($ram == 0) {
    if ($numProcs < 12) {
	$ram = $ramPerProc * $numProcs;
    } else {
	$ram = $MAX_DEFAULT_RAM;
    }
} elsif ($ram > $ramPerProc && $numProcs == 1 && ! $smpOnly) {

    my $d = int($ram / $ramPerProc);
    my $m = $ram % $ramPerProc;
    $numProcs = $d;
    if ($m) {
	$numProcs++;
    }
    if ($numProcs > $MAXCPUS) {
	$numProcs = $MAXCPUS;
    }
}


my $cpuTime = $wallTime * $numProcs;


# what group is this submitted under?
if ($group eq '') {

    my @va = `va`;
#    my @va = `cat  /scratch/test`;
    my $failed=1; # attempt to find the group with remaning hours in it
    for (my $i= $#va; $i >= 0; $i--) {
	my @s = split /[\t \/:]+/, $va[$i]; 
	last if ($s[0] eq 'Group');

	my ($g, $h) = @s; # group name, hours (in the standard queue)
	if ($queue =~ m/windfall/i) {
	    $group = $g; # doesn't matter which group
	    last;
	} elsif ($queue =~ m/high/i) {
	    $h = $s[7]; # hard-coded;this may break. this should correspond to the column of the number of hours in the high priority queue
	    if (!defined $h) {
		die "You asked for high priority hours, but it looks like you have none!\n";
	    }
	}

	if ($h >= $cpuTime) {
	    $group = $g; # greedily search for the first group that has enough hours
	    last;
	}

    }

    if ($group eq '') {
	die "I failed to find enough hours in queue: $queue\nI estimated that you would need $cpuTime cpu-hours\n";
    }

    if (0) { # old hack to find the appropriate group.
	my $ret = `groups`;
	my @s = split /\s+/, $ret;
	if (@s > 1) {
	    $group = $s[1]; # for whatever reason, this picks a good group! (nrsc appears to be the 0th item...)
	} elsif (@s == 1) {
	    $group = $s[0];
	} else {
	    die "The unix command 'groups' did not return any groups for you... that's not good!\n";
	}
    }
}




print "#!/bin/bash\n";
if ($name) {
    print "#PBS -N $name\n";
}
print "#PBS -W group_list=$group\n";
if ($clusterOnly) {
    print "#PBS -l jobtype=cluster_only\n";
} elsif ($htcOnly) {
    print "#PBS -l jobtype=htc_only\n";
} elsif ($smpOnly) {
    print "#PBS -l jobtype=smp_only\n";
} else {
    print "#PBS -l jobtype=small_mpi\n";
}

print "#PBS -l select=1:ncpus=$numProcs:mem=$ram" , "mb";


if ($numProcs < $MAXCPUS) {
    print "\n#PBS -l place=pack:shared\n";
} elsif ($ram > $MAX_DEFAULT_RAM) {
    if (! $smpOnly) {
	if ($ram <= 2*$MAX_DEFAULT_RAM) { # this is requesting one of the high-memory nodes on the HPC
	    print ":pcmem=4gb\n";
	} elsif ($ram <= 4*$MAX_DEFAULT_RAM) {
	    print ":pcmem=8gb\n";
	} else {
	    die "This is too much memory for the non-SMP nodes to handle! Rerun me w/ the -s flag!\n";
	} 
    } else {
	print "\n";
    }

} else {

    print "\n";
}

# set the virtual memory requirements. If this is not set some JAVA/Python jobs choke.
print "#PBS -l pvmem=" , $ram * 3 , "mb\n";

print "#PBS -l cput=$cpuTime:00:0\n#PBS -l walltime=$wallTime:00:0\n";
print "#PBS -q $queue\n";

if ($email ne '') {
    print "#PBS -M $email\n#PBS -m bea\n";
}

if ($join) {
    print "#PBS -j oe\n";
}

print "\n";
foreach (@modules) {
    print "module load $_\n";
}


print "\n\ncd \$PBS_O_WORKDIR\n\n@ARGV\n";



