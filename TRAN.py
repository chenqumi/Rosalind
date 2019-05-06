'''
chenqumi@20180815
Transitions and Transversions

transition:
substitution between purine OR pyrimidine
A <--> G, C <--> T
transversion: 
interchange of a purine for a pyrimidine
A <--> T, A <--> C, C <--> G, G <--> T

Across the entire genome,
the ratio of transitions to transversions is on average about 2.
In coding regions, this ratio is typically higher (>3)
'''
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


baseType = {
    'A': 'purine',
    'C': 'pyrimidine',
    'G': 'purine',
    'T': 'pyrimidine',

}
def ratioTran(s1, s2):
    '''
    s1 has the same length with s2
    '''
    trans = {
        'transition': 0,
        'transversion': 0,
    }
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        if baseType[s1[i]] == baseType[s2[i]]:
            trans['transition'] += 1
        else:
            trans['transversion'] += 1
    return trans['transition']/trans['transversion']


faDic = {}
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            faDic[ids] = ''
        else:
            faDic[ids] += line

s1, s2 = faDic.values()
print(ratioTran(s1, s2))
