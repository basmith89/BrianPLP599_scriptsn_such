__author__ = 'briansmith'

#This script will intake a file and report the highest GC
#content out of the sequences provided

data = ""
seqID = []
nuc_list = []

#readlines reads lines one by one
f = open('rosalind_gc.txt', 'r').readlines()

for line in f:
    line = line.strip()
    for i in line:
        if i.startswith(">"):
            seqID.append(line[1:])
            #if data == True statement and opens up the ability to read the nuc lines
            if data:
                nuc_list.append(data)
                data = '' #resets data to empty string add more seqs
            break #restarts loop after list entry has been made
        else:
            line = line.upper() #I don't think this is necessary
    #stores all lines of seq in data here
    if all([k == k.upper() for k in line]):
        data += line

#The last seq has not yet been added so append once more
nuc_list.append(data)


GC_list = []
for seq in nuc_list:
    i = 0
    for k in seq:
        if k == "G" or k == 'C':
            i += 1
    GC_cont = float(i)/len(seq)*100.0
    GC_list.append(GC_cont)

#looks for max value and prints the corresponding index
m = max(GC_list)
print seqID[GC_list.index(m)]

#prints the seq with the highest GC content.
#format notation :0.6 prints out to six decimal places
#f is for floating point numbers
#"{:}" syntax
print "{:0.6f}".format(m)