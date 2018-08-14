#chenqumi@20180720
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Enumerating Gene Orders
'''
import os
import re
import sys
import math
import itertools


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

n = sys.argv[1]
n = int(n)

def permutate(n):
    print(math.factorial(n))
    for comb in itertools.permutations(range(1, n+1), n):
        tmp = [str(i) for i in comb]
        print(' '.join(tmp))

permutate(n)