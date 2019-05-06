'''
chenqumi@20180815
Speeding Up Motif Finding
The failure array of s is an array P of length n for which 
P[k] is the length of the longest substring s[j:k] 
that is equal to some prefix s[1:k−j+1], where j CANNOT equal 1 
(otherwise, P[k] would always equal k). By convention, P[1]=0
'''
import os
import re
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


def failureArr(seq):
    P = [0,]
    for k in range(1, len(seq)):
        subSeq = seq[:k+1]
        length = [0,]
        for j in range(1, k+1):
            if seq[j:k+1] == seq[:k-j+1]:
                length.append(k-j+1)
        P.append(max(length))
    return P


def fArray(seq):
    P = [0,]
    for k in range(1, len(seq)):
        subSeqlen = k+1
        subSeq = seq[:subSeqlen]
        div, mod = divmod(subSeqlen, 2)
        mid = div + mod
        lenArr = [0,]
        for j in range(mid, subSeqlen):
            prefix = subSeq[:subSeqlen-j]
            suffix = subSeq[j:]
            if prefix == suffix:
                lenArr.append(subSeqlen-j)
        P.append(max(lenArr))
    return P


ids = ''
faDic = {}
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            faDic[ids] = ''
        else:
            faDic[ids] += line

seq = faDic[ids]
for i in fArray(seq):
    print(i, end=' ')
