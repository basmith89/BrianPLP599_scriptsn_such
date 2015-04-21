#!/bin/bash

#By Brian Smith, University of Arizona
#Quick script to remove newlines from a fasta file.


awk '/^>/{print s? s"\n"$0:$0;s="";next}{s=s sprintf("%s",$0)}END{if(s)print s}' pMP.fasta

#last part is just input file and will need to be changed
