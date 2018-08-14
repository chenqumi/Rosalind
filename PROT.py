#chenqumi@20180720
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Translating RNA into Protein
'''
import os
import re
import sys
import json


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

seq = sys.argv[1]


codonTable = json.load(open('codonTable.json'))


def rna2pro(seq):
    pro = ''
    i = 0
    while i < len(seq):
        codon = seq[i:i+3]
        pro += codonTable[codon]
        i += 3
    return pro


print(rna2pro(seq))