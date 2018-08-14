#chenqumi@20180725
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Open Reading Frames
'''
import os
import re
import sys
import json

if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

file = sys.argv[1]


codonTable = json.load(open('codonTable.json'))


comp = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}


def revComplement(seq):
    revc = ''
    for i in range(len(seq)-1, -1, -1):
        revc += comp[seq[i]]
    return revc


def ORF(seq, init):
    seq = seq.replace('T', 'U')
    i = init
    prot = ''
    orfs = set()
    translate = False
    while i <= len(seq)-init-3:
        codon = seq[i:i+3]
        if codon == 'AUG':
            translate = True
        if codon in ('UAA', 'UAG', 'UGA'):
            translate = False
            if prot != '':
                orfs.add(prot)
            prot = ''
        if translate:
            prot += codonTable[codon]
        i += 3
    return orfs


'''
regex = re.compile(r'M')
it = regex.finditer(prot)
startPos = [i.start() for i in it]
'''
def spliceORF(orf):
    tmp = set()
    it = re.finditer(r'M', orf[1:])
    startPos = [i.start()+1 for i in it]
    for pos in startPos:
        tmp.add(orf[pos:])
    return tmp


# with open(file) as fd:
#     seq = ''
#     for line in fd:
#         line = line.strip()
#         if line.startswith('>'):
#             continue
#         seq += line

# ORFs = set()
# for i in range(3):
#     ORFs |= ORF(seq, i)
#     ORFs |= ORF(revComplement(seq), i)


# tmp = set()
# for orf in ORFs:
#     tmp |= spliceORF(orf)


# ORFs |= tmp
# for orf in ORFs:
#     print(orf)
