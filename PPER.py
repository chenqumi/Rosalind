'''
chenqumi@20180811
Partial Permutations
'''
import sys
from math import factorial


if len(sys.argv) == 1:
    print("\nUsage: {} <n> <k> ".format(sys.argv[0]))
    sys.exit()

n, k = sys.argv[1:3]
n = int(n)
k = int(k)


def partialPerm(n, k):
    '''
    k elements full permutation:  k!
    from n elements select k :    C(k,n) = n!/(k! * (n-k)!)
    '''
    P_nk = factorial(n)/factorial(n-k)
    return int(P_nk % 1000000)


print(partialPerm(n, k))