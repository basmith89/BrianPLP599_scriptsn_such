#!/usr/bin/python

seq = "GCTGCCTTAGGGCGGGTCAACCTATCTCAAGTTGGGGCAAGTTAGGAAACTGACTATATACGGAGATCAGAAATTCACGTCCCGTCAGAAAGAGGGCCCATTTAACAGAGCTTTCGCGGTGTATGCCCCTACGACTCTTATGTCTACTCGCCCCTATGACAGGCTACGACCTTACTAATGCGAATCCAAAGGCTCACTAGTCGACCGGAATCTGGTTTTCCACATGTACTATCAAAACGAAATAGTGCCTATGCGGTCCGCGCAATATAGGTCAATCAGCCGGTGTCGTTAGAGGCCTACCGCAGGCAGAAATTACGTTTATGTCCAATGCTCTCCTAGTCATCCAAATGGGTGGTGACCTCTCTATCGCCCTTTTGAGATCGCAAGAGCCCAGACGGGTTGCTACCCGGTCTAGTATGTAACAATTTGGCGATAGGCTAGTACGATATCTTTTCCCAGCATATTATATACATACGACAACCTAACAGTCTCATATAGCTACAGGAGACCGGTGATAGTATCTTCTATTCGGCCTTCCCTACCCCGCTCCCCTTTGAACAGACTCAGTGATTAGCTCGCGAGTTCCTAGCGCGAGTCGACTAACAAAGTAGGTGTACTGCACACAAAGACCTTGATATAGTGTCCTCCGCGATATTAGTCGCGTTTCTCCAATGGCTTGCCAGTGGGACAACGCAAATTACGGTTTAGAAAGCACATGGTCTAACAATAGGCGGGAGCAGACGTCCGGCGGTCTTCCTCCGTTGTGTACTAAAGGAACAACAGTAGATTTGTCATCTAATGACTAGACTCTTCTTATAATATGCCAGAATTGGAACATGGAGCTTACGACGGTACTCACGGCCGACGTTGGCTTCAGTCGCGCTTAGTAGTCTTAGAATGTTCTGGCACCACGCGGGCCCATTGCGATCAACTTAATAGCAACCTTCCCGTTGGTCACTCCGCCG"  #add sequence here or edit to take input

Acount = 0
Tcount = 0
Ccount = 0
Gcount = 0

for C in seq:
	if C == "A":
		Acount = Acount + 1
	elif C == "C":
		Ccount = Ccount + 1
	elif C == "T":
		Tcount = Tcount + 1
	elif C == "G":
		Gcount = Gcount + 1

print Acount, Ccount, Gcount, Tcount