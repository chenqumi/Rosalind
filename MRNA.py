#chenqumi@20180725
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Inferring mRNA from Protein
'''
import os
import re
import sys
import json


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

seq = sys.argv[1]


def pro2codon(pro):
    return len(cTable[pro])


codonTable = json.load(open('codonTable.json'))


cTable = {}
for codon, pro in codonTable.items():
    cTable.setdefault(pro,[]).append(codon)

# 3 stop codon not present in pro seq,
# but in mrna seq    
mrna = 3
for pro in seq:
    mrna *= pro2codon(pro)

print(mrna%1000000)
