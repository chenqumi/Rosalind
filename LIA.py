#chenqumi@20180724
#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Independent Alleles
Mendel's second law
'''
from scipy.special import comb


def lia(k, n):
    '''
    k: k-th generation offsprings
    n: at least n AaBb offsprings in all k-th generation
    ancestor is 0-th generation
    P(x=AaBb) = 0.25
    P(x!=AaBb) = 0.75
    for k=2, n=1, there are 4 offsprings,
    prob = C1,4 * 0.25**1 * 0.75**3 + C2,4() + C3,4() + C4,4()

    actually, it's a Binomial Distribution
    '''
    offsprings = 2**k
    prob = 0.0
    for i in range(n, offsprings+1):
        prob += comb(offsprings, i) * (0.25**i) * (0.75**(offsprings-i))

    return prob


print(lia(5, 8))
