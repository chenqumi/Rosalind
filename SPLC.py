#chenqumi@20180726
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
RNA Splicing
'''
import os
import re
import sys
from ORF import ORF


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


def rnaSplicing(rna, intronList):
    for intron in intronList:
        rna = rna.replace(intron, '')
    return rna


seq = ''
seqList = []
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            if seq != '':
                seqList.append(seq)
                seq = ''
        else:
            seq += line
    seqList.append(seq)

rna = rnaSplicing(seqList[0], seqList[1:])
# print(rna)
for i in ORF(rna, 0):
    print(i)