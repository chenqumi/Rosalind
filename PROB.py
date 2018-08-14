'''
chenqumi@20180811
Introduction to Random Strings
'''
import math
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <rosalind_prob.txt> ".format(sys.argv[0]))
    sys.exit()

file = sys.argv[1]


def prob(seq, gcContent):
    P_gc = gcContent/2
    P_at = (1-gcContent)/2
    probDic = {
        'A': P_at,
        'C': P_gc,
        'G': P_gc,
        'T': P_at,
    }
    prob = 1.0
    for base in seq:
        prob *= probDic[base]
    return str(math.log(prob, 10))


seq = ''
gcArr = []
with open(file) as fd:
    for line in fd:
        seq = line.strip()
        gcArr = fd.readline().strip().split()

result = [prob(seq, float(gcContent)) for gcContent in gcArr]
print(' '.join(result))