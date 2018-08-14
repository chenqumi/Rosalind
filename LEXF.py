#chenqumi@20180726
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Enumerating k-mers Lexicographically
'''
import itertools as it


def product(iters, n):
    for comb in it.product(iters, repeat=n):
        print(''.join(comb))


product('ABCDEFG', 3)