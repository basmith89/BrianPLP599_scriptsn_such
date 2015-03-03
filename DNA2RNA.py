#!/usr/bin/python

seq = "CACTAAACAAACTACATGACGTTATAAGGCAGTTGTGTCCATTTCTCCAATTTGTTCATATGAACAGCGCATACGAGAGCTCGCACTATGGACATAGTGAGCGCCTTGTACTGTGCCTGCGGCCAACCAACCGTGTACTCTCGTGTGTACGACTCTGACGACCATACTCACGGGATTATTGACTCGAACGACTTTACGTACTTCCGTGTATACGACCACACACACCTCGGTCCATCATTTTGCCAGCAATTTCGAGGGATCTTTCCGCTTCAGATCTTAGGGGGCAGGCTTGTTTTTCTGACAGCACATCCTAGGTCAGAAGACTTCGTGCTAAAGTGTGGTAATGAAAACATATCAGTTAACGAAGCAGGTCGTCGAAAGGGCACGGTTCCGTATACCATCATACGGCCTAACTCGGATATACGCTCGCTAGCCCTTGACGTCTAAAATTGCCCGCCCGTTACATTACATCACCATGCTGCATAATTTGGAATTCCATGGCGCAAGGTGATCACAATCGTCTACAATTTTGTGGAGGAGCGGGGTTCCGGGTAGGGGCTCGGCTTCTATTTGCAACTAACCTTCTGGCTAATTAGGCGTCGACTAAACAGATGTATGTTCCGCTATATCACGGCCATTGGAGGAAGTCGCATTGGACTTTGAACAAATCGAGTAGATGCCCCGCGCACGTGTGGGGGGTGCGGTCCGCGTTGGTCTATATTATTTTAACTCTGGCTCTCTGGGGAGTGATCGCGGTTCAAAGTCTTATTTAAAAGGACAAAGGTGTTCGGGTCAGACACGAGGACTACGCTTCCTCTCGGTTAGCACCGACAAGGCCACCATCACGGTAAAATTCGGCGCACCTAACGTTTGCTACGAAGTGGACCGGACGCCCCAGTGGCTTTGTGTACTCCAAAGCAGACAGCATTATTTATCAGGGAGCCAGG"
  #add sequence here or edit to take input


def transcribe(seq):
	#Return DNA string as RNA
	return seq.replace("T","U")

print transcribe(seq)


