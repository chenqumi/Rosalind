#chenqumi@20180723
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Finding a Most Likely Common Ancestor
'''
import os
import re
import sys
import collections


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


seq_dict = {}
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            seq_dict[ids] = ''
        else:
            seq_dict[ids] += line

'''
msa = {
    0:{
        'A': 5,
        'C': 3,
    },
    1: {
        'A': 1,
        'C': 6,
    },
}
'''
msa = collections.OrderedDict()
for seq in seq_dict.values():
    for idx, base in enumerate(seq):
        msa[idx][base] = msa.setdefault(idx, {}).get(base, 0) + 1

consensus = ''
cntA = ['A:',]
cntC = ['C:',]
cntG = ['G:',]
cntT = ['T:',]
# for i in 'ACGT':
for pos, bases in msa.items():
    cntA.append(str(msa[pos].get('A', 0)))
    cntC.append(str(msa[pos].get('C', 0)))
    cntG.append(str(msa[pos].get('G', 0)))
    cntT.append(str(msa[pos].get('T', 0)))
    tmp = sorted(bases.items(), key=lambda x:x[1], reverse=True)
    consensus += tmp[0][0]
print(consensus)
print(' '.join(cntA))
print(' '.join(cntC))
print(' '.join(cntG))
print(' '.join(cntT))