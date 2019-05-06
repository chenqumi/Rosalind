'''
chenqumi@20180814
Finding a Spliced Motif
'''
import collections
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <rosalind.txt> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


def spliceMotif(s, t):
    '''
    symbols of t appear as a subsequence of s
    '''
    result = []
    initPos = 0
    for symbol in t:
        idx = s[initPos:].index(symbol)
        result.append(str(idx + initPos + 1))
        # avoid homopoly, ATCGGGG
        initPos += (idx+1)
    return ' '.join(result)


faDic = collections.OrderedDict()
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            faDic[ids] = ''
        else:
            faDic[ids] += line

s, t = faDic.values()
print(spliceMotif(s, t))

