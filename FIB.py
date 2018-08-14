'''
Rabbits and Recurrence Relations
'''
import sys


def Rabbits(n, k):
    '''
    n: n-th generation
    k: k pairs offsprings per pairs of rabbits
    '''
    if n <= 2:
        return 1
    else:
        return Rabbits(n-2, k)*k + Rabbits(n-1, k)


n, k = sys.argv[1:3]
n = int(n)
k = int(k)
print(Rabbits(n, k))