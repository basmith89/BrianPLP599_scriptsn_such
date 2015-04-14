__author__ = 'briansmith'

import collections
import re
import pprint


# Created By: Brian A. Smith, University of Arizona
# Version 1.1.6
# origin of replication motifs are about 8-9 nucleotides in size
# in E. coli there are 4 DNaA boxes with this conserved motif

InFileName = "test.txt"
open_file = open(InFileName, 'r').readlines()
dna = ""

#Looping through file and storing sequence data in dna
for line in open_file:
    if not line.startswith(">"):
        line = line.strip('\n')
        dna += str(line)
        print dna



#This function will slide through the sequence based off 'k'mer size
#and will store the motifs as a key in a dictionary with which holds a new dictionary
#containing counts and position of those counts
#It also uses a min % calculation to filter out low occurances.  Use 0 to see all motifs


def motif_count(dna, k, minimum_percentage):
    total_kmers = len(dna) - k + 1
    minimum_count = (total_kmers * minimum_percentage) / 100
    print "Min count is: %s"  %(str(minimum_count))
    #create a dictionary of motifs
    motifs2count = {}
    for x in range(len(dna)+1-k):
        #this is the sliding window of length k
        kmer = dna[x:x+k]
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
    print "Total number of motifs found: %d" %(len(motifs2count))
    return motifs2count

print motif_count(dna, 3, 0)
pprint.pprint(motif_count(dna, 3, 0))

###start motif_list process
#This function stores motifs in a list so collections can be used to sort them
def motif_list(dna, k):
    result = []
    for x in range(len(dna)+1-k):
            result.append(dna[x:x+k])
    return result

my_list = motif_list(dna, 3)
#Counts up motifs in list then prints top N common motifs
c = collections.Counter(my_list)
print "Top Motifs:"
print(c.most_common(3))
###end motif_list process

