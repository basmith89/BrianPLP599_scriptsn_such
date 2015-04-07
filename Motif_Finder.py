__author__ = 'briansmith'

import collections
import re
from collections import defaultdict

# Created By: Brian A. Smith, University of Arizona
# Version 1.1.2
# origin of replication motifs are about 8-9 nucleotides in size
# in E. coli there are 4 DNaA boxes with this conserved motif
dna = "AGTCGTGGCATGGTAGTTTTATGATGATGTTGTTG"



#This function will slide through the sequence based off 'k'mer size
#and will store the motifs as a key in a dictionary with the number of times present as its value
#It also uses a min % calculation to filter out low occurances.  Use 0 to see all motifs
def motif_count(dna, k, minimum_percentage):
    total_kmers = len(dna) - k + 1
    minimum_count = (total_kmers * minimum_percentage) / 100
    print "Min count is: %s"  %(str(minimum_count))
    #create a dictionary of motifs
    motifs2count = {}
    for x in range(len(dna)+1-k):
        kmer = dna[x:x+k]
        #kmer_match = re.match(kmer_find, dna)
        #counts up motifs and stores as a dict value
        motifs2count[kmer] = motifs2count.get(kmer, 0) + 1

    motif_positions = {}
    print "Motif positions:"
    for x in range(len(dna)+1-k):
        kmer = dna[x:x+k]
        motif_positions[kmer] = []
        kmer_find = re.compile(re.escape(kmer))
        for match in re.finditer(kmer_find, dna):
            #span gets the start and end positions for regex
            motif_positions[kmer].append(match.span())
            #for element in motif_positions[kmer]:
             #   new_val = element + 1
              #  motif_positions[kmer].append(new_val)





    #Selecting only high-count kmers
    #.items calls the dictionary's keys and values
    for kmer, count in motifs2count.items():
        if count < minimum_count:
            del motifs2count[kmer]
    print "Total number of motifs found: %d" %(len(motifs2count))
    return motifs2count


def motif_list(dna, k):
    result = []
    for x in range(len(dna)+1-k):
            result.append(dna[x:x+k])
    return result


my_list = motif_list(dna, 3)

#Counts up motifs in list then prints top N common motifs
c = collections.Counter(my_list)
#print(c.most_common(3))

print motif_count(dna, 3, 0)
