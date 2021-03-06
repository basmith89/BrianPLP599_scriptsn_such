__author__ = 'briansmith'

#import regex library
import re

seq = "CCCGCGGGCCCGCGGTTCCCCGCGGTCCCGCGGCCCGCGGAGCCCCGCGGCCCGCGGCCCGCGGGCCCGCGGTCCCGCGGCCCCGCGGAACCCGCGGCCCCGCGGCTACAAGCCCCGCGGTCCCGCGGCCCGCGGCCCGTGGACCCCGCGGTCCCGCGGACCCGCGGCATTCGCCCGCGGCCCGCGGGAAATATGCCCGCGGCCCGCGGCCCGCGGTGAGACCCGCGGCCCGCGGACCCGCGGCTGTCCCGCGGTCCCGCGGACCCGCGGATTTTGATCCCGCGGACCCGCGGGTCAAATAGCCCCGCGGCATCCCCGCGGATAACCCGCGGTCACCCGCGGCCCGCGGCCTACATTCTAAAGGCCCGCGGACCCGCGGCTTCTCCCGCGGCCCGCGGCCCGCGGGCCCCGCGGACCCGCGGTGACCCGCGGATACCCGCGGACCCGTTCCCGCGGGCCCGCGGCCCGCGGCCCGCGGTCCCCGCGGGAGGGTATCGATTCCACCCGCGGCCCGCGGCAAACCCGCGGAATTCCCGCGGTCCCGCGGCCCGCGGACTGAGCCCCGCGGGTCCTCACGGCCCGCGGCCCGCGGCCCGCGGAGAGCCCGCGGTACCCGCGGCCCGCGGCTTTCCATCCCGCGGAACCCCGCGGATCAGTTTCCCGCGGCCCGCGGCCCGCGGCCCCGCGGCCCGCGGTGTAAGGTGCCCGCGGTTCCCCGCGGCCCGCGGAGGCAGCCCGCGGCATTCAGATGCCCGCGGTCCCGCGGAGCCCGCGGCCCGCGGTCCCCGCGGTACCCGCGGTTCCCGCGGAGTCCCGCGGTAGCCCGCGGTCTCCCGCGGCCCGCGGCTTCTTGCGCTCCCGCGGACTGATCCCGCGGCCCGCGGCCCGCGGTGG"
motif = "CCCGCGGCC"

#Insert motif after (?=(
#matches motifs using finditer. finditer return the number where the motif
#started.  Matches left to right and non-overlapping
#(?=( allows for overlapping motifs
matches = re.finditer(r'(?=(CCCGCGGCC))', seq)


#uses the regex library to start at postion 0 and finds
found = [item.start(0) + 1 for item in matches]

print found
