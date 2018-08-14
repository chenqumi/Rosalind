#chenqumi@20180725
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Finding a Protein Motif
'''
import os
import re
import sys
from urllib import request

if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

file = sys.argv[1]


def getData(protid):
    url = f'http://www.uniprot.org/uniprot/{protid}.fasta'
    data = request.urlopen(url).read().decode('utf8')
    seq = ''.join(data.split('\n')[1:])
    return seq


def findMotif(seq, pattern=r'(?=N[^P][ST][^P])'):
    it = re.finditer(pattern, seq)
    startPos = [str(i.start()+1) for i in it]
    return startPos


with open(file) as fd, open('mprt.fasta', 'w') as O:
    for line in fd:
        protid = line.strip()
        seq = getData(protid)
        O.write(f'>{protid}\n')
        O.write(seq+'\n')
        startPos = findMotif(seq)
        if startPos == []:
            continue
        print(protid)
        print(' '.join(startPos))
