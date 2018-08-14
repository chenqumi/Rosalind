#chenqumi@20180724
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Finding a Shared Motif
'''
import os
import re
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <rosalind.fasta> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


def makeKmer(seq, k):
    s = set()
    for i in range(len(seq)-k+1):
        kmer = seq[i:k+i]
        s.add(kmer)
    return s


seqDict = {}
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            seqDict[ids] = ''
        else:
            seqDict[ids] += line


tmp = sorted(seqDict.items(), key=lambda x:len(x[1]))
shortestSeq = tmp[0][1]
otherSeq = [i[1] for i in tmp[1:]]


# for i in makeKmer(shortestSeq, 4):
#     print(i)


motif = []
k = len(shortestSeq)
while k > 1:
    for kmer in makeKmer(shortestSeq, k):
        found = True
        for seq in otherSeq:
            if kmer not in seq:
                found = False
                break
        if found == True:
            motif.append(kmer)
    if len(motif) != 0:
        break
    else:
        k -= 1

if len(motif) > 0:
    for i in motif:
        print(i)
else:
    print('no motif')