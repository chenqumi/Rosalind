'''
chenqumi@20180813
Enumerating Oriented Gene Orderings
'''
import sys 
from math import factorial
from itertools import permutations, product
import operator


if len(sys.argv) == 1:
    print("\nUsage: {} <num> ".format(sys.argv[0]))
    sys.exit()

num = sys.argv[1]
num = int(num)


def signPerm(num):
    total = factorial(num) * (2 ** num)
    print(total)
    for order in permutations(range(1, num+1), num):
        for sign in product('+-', repeat=num):
            signedOrder = combTuple(order, sign, num)
            print(' '.join(signedOrder))


def combTuple(order, sign, num):
    '''
    order is a num tuple,    ( 1,   2 )
    sign is a symbol tulple, ('+', '-')
    '''
    signDic = {
        '+': operator.pos,
        '-': operator.neg
    }
    return [str(signDic[sign[idx]](order[idx])) for idx in range(num)]


signPerm(num)