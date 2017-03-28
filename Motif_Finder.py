#!/usr/bin/env python

__author__ = 'briansmith'

import collections
import re
import pprint
import time
import sys
import argparse, textwrap


#notes: could make math better so the progress bar updates every 5% and adds a single bar
#       eventually remove debugging print statements.


# origin of replication motifs are about 8-9 nucleotides in size
# in E. coli there are 4 DNaA boxes with this conserved motif

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description = textwrap.dedent('''\
                                 Author: Brian A. Smith
                                 University of Arizona
                                 basmith@email.arizona.edu
                 Motif Finder
                 Version 1.2
                 This motif finder will use a brute force method to count common motifs
                 and report the top 10 to STDOUT.  A full report will also be written to
                 desired output file.'''))

parser.add_argument("-i", "--input", required = True,
           help = "FASTA file required")
parser.add_argument("-o", "--output", required = True,
                    help = "Desired output file name")
parser.add_argument("-s", "--start_slice", required = False,
                    type = int, help = "Select a starting position to cut [START:end:step]")
parser.add_argument("-e", "--end_slice", required = False,
                    type = int, help = "Select an ending position to cut [start:END:step]")
parser.add_argument("-m", "--motif_size", required = True,
                    type = int, help = "Choose a desired motif size")

args = parser.parse_args()

open_file = open(args.input, 'r')
write2file = open(args.output, 'w')
dna = ""

print "Start: ", time.clock()

if args.start_slice:
    start_slice = args.start_slice - 1
    print start_slice
    print args.end_slice

# Looping through file and storing sequence data in dna
for line in open_file.readlines():
    if not line.startswith(">"):
        if args.start_slice and args.end_slice:
            line = line.strip('\n')[start_slice:args.end_slice]
        elif args.start_slice:
            line = line.strip('\n')[start_slice:]
        elif args.end_slice:
            line = line.strip('\n')[:args.end_slice]
        else:
            line = line.strip('\n')
        #line = line.strip('\n')[1:100000]
        #line splice to desired position of seq or delete for entire seq
        dna += str(line)
        print dna

print "First loop: ", time.clock()

#This function will slide through the sequence based off 'k'mer size
#and will store the motifs as a key in a dictionary with which holds a new dictionary
#containing counts and position of those counts
#It also uses a min % calculation to filter out low occurances.  Use 0 to see all motifs



def motif_count(dna, k, minimum_percentage):
    total_kmers = len(dna) - k + 1
    minimum_count = (total_kmers * minimum_percentage) / 100
    print "Min count is: %s" % (str(minimum_count))
    #create a dictionary of motifs
    motifs2count = {}
    print "Collecting motifs: "
    #the following variables are for building the progress bar
    seq_list = range(len(dna) + 1 - k)
    total_nuc = seq_list[-1]
    pbar_total = round(total_nuc, -1)
    print "Creating motif library, please wait.\n" \
          "If it's a large sequence, brew some coffee and come back later :)"

    for x in seq_list:
        bar_percent = int((x/pbar_total)*10)
        bar = int(((x/pbar_total)*10)*2)
        #print x/pbar_total
        #convert value ^ into a var, add if statement with modulous, lookup floor function
        #have to do math on total val so it will print multiple times
        if ((x/pbar_total)*100) % 10 == 0:
            sys.stdout.write('\r')
            #Can't get it to print to 100% in increments of 5 with each = being 5%
            sys.stdout.write("[%-20s] %d%%" % ('='*bar, 10*bar_percent))
            sys.stdout.flush()

        #print progress bar
        #this is the sliding window of length k
        kmer = dna[x:x + k]
        #open an empty list for position lists .span
        position = []
        #create varible for regex to find kmer
        kmer_find = re.compile(re.escape(kmer))
        #for loop searching for how many times selected kmer occurs in a sequence
        for match in re.finditer(kmer_find, dna):
            #span gets the start and end positions for regex
            #span makes tuples therefore it must be converted to a list to add 1 to get starting position of 1 not 0
            hit = list(match.span())
            hit[0] += 1
            hit[1] += 1
            position.append(hit)


        motifs2count[kmer] = {"Count": dna.count(kmer), "Position": position}

    #Selecting only high-count kmers
    #.items calls the dictionary's keys and values
    for kmer, count in motifs2count.items():
        if count < minimum_count:
            del motifs2count[kmer]
    print "\nDone!\nTotal number of motifs found: %d" % (len(motifs2count))
    return motifs2count

#print motif_count(dna, 3, 0)
pprint.pprint(motif_count(dna, args.motif_size, 0), write2file)

###start motif_list process
#This function stores motifs in a list so collections can be used to sort them
def motif_list(dna, k):
    result = []
    for x in range(len(dna) + 1 - k):
        result.append(dna[x:x + k])
    return result


my_list = motif_list(dna, args.motif_size)
#Counts up motifs in list then prints top N common motifs
c = collections.Counter(my_list)
print "Top Motifs:"
print(c.most_common(10))
###end motif_list process



print "Done: ", time.clock()

