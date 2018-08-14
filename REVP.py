#chenqumi@20180726
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Locating Restriction Sites
'''
import os
import re
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

file = sys.argv[1]


complement = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}
'''
reverse palindrome meets:
1. length is even
2. seq[idx] is complemet with seq[len-1-idx],
   like a DeQueue
'''
def revPalindrome(seq):
    l = len(seq)
    mid = (l-1) // 2
    revPal = True
    for i in range(mid+1):
        if complement[seq[i]] != seq[l-1-i]:
            revPal = False
            break
    return revPal


with open(file) as fd:
    seq = ''
    for line in fd:
        line = line.strip()
        if line.startswith('>'):
            continue
        seq += line


for length in range(4, 13, 2):
    for i in range(len(seq)-length+1):
        fragment = seq[i:length+i]
        if revPalindrome(fragment):
            print(i+1, length)
