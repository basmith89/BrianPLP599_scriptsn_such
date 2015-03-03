#!/usr/bin/python

seq = "TCTTAACCCTTGGATCGGTGTTCTGTTATGGGATCCGGTACTGGACCCCCGTGTACGCGCTTGGAGTCTGTGATAACGAAAGGAAACTGGGTCCGACTGATGCATCGCTGCCTGCAGTGACACTAATCTGGGACGACCTGACCACGTGTCTGAACACACTACATCCTTTCCAACTTTCGTTTTCAGGCGCGTGACGCCTTGGTATTCCTAGGGGTAAAGTTTCGCGGACTGGAGCACTGATTTACCTACTTTTAACGATCGCTGTACAAGATGGCTTGTGCCCTCAATTACTTGGAGTCTACCACGATCTTAGAGTGAGCATTCTGGACGCTAGTCACACAAACTATGTTGCGACAAGGGTTTCGATGGGCCCGGACAGTGATGTAACTGTGTCAATCTTACTCATCTGATCAATGGGCATTAATTTTATCAAGCTGGATGTCCGGAAAGGAAGTTATACTAGGAGCCTATTAGGAAGGCCTCCTTCCAGGAATTTCCATCAGTGCGCGCATAGTATCCGTATGCCGTTTAGTTTGATCCCTCCTTGCTGGCCGTCTGGACCCTCCTGCTTTCCAATTGGCATCTTGCCCAGCTTCGCGCAGAGTAGATGGCATGTCAGATAGAGTTACCGCTTATTTCAGGCCTGAGACTTCCGTTAAGATGGTAGGTTTCTCTTGGAAATTGGCAAATCCTAGGTGCCACCGAAAAATATAGGGAATCCTTTAAGACGACTGCATGAGTCGTCCTCATGCAGCTGGGGGGATTACTTAGGGCCTTGCGCATATGATAAATTTAAAGGTTAGATATTCGCCACGCCCGGCCACCATACCCACCGTTTATGCCTGGATTACTGTGGTATTTCGGATTTAATTCGATTTCAGCTCCTTCAGAACACCGTCAGAC"
  #add sequence here or edit to take input


def complement(seq):
	#Reverse and complement DNA strand
	basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
	bases = list(seq) #creates of list of bases from seq stored in bases
	bases = [basecomplement[base] for base in bases] 
	return ''.join(bases)

		
#Reverse seq with list slicing method
print complement(seq)[::-1]



