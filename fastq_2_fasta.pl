#!/usr/bin/env perl
use warnings;
use strict;

#Ensure In/Out files are made when running the script in command line
open(IN,"<$ARGV[0]")|| die;
open(OUT,">$ARGV[1]")|| die;


while (my $line = <IN>) {
chomp $line;
	$line =~ s/^@/'>/g;             #replace @ notation with >
	$line =~ s/[~!%^&*()_+|}{"?^`\]\[\\< ]*//g;      #remove special characters in quality score 
	$line =~ s/[a-z]//g; 			#remove any lower case letters in quality score
	$line =~ s/^\w*[^ACGT>]//g;		#remove any starting characters that are not nucleotides or >
	$line =~ s/\s//g;
	print (OUT "$line \n");        #write the file
}

close (IN);
close (OUT);

	