__author__ = 'briansmith'

import collections

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
        motifs2count[kmer] = motifs2count.get(kmer, 0) + 1

    #Selecting only high-count kmers
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
c = collections.Counter(my_list)

print(c.most_common(3))
print motif_count(dna, 3, 0)
