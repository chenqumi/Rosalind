#chenqumi@20180720
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Finding a Motif in DNA
'''
import os
import re
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

file = sys.argv[1]


def makeKmer(seq, motif):
    d = {}
    k = len(motif)
    for i in range(len(seq)-k+1):
        kmer = seq[i:k+i]
        d.setdefault(kmer, []).append(str(i+1))
    return ' '.join(d[motif])


with open(file) as F:
    seq = F.readline().strip()
    motif = F.readline().strip()

print(makeKmer(seq, motif))
