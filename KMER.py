'''
chenqumi@20180815
k-mer Composition
A genomic region having high GC-content compared to the rest of the genome
signals that it may belong to an exon.
'''
import collections
import itertools
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


def kmerCount(seq, k=4):
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        kmerDic[kmer] = kmerDic.get(kmer, 0) + 1
    # return kmerDic


kmerDic = {}
faDic = {}
ids = ''
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            faDic[ids] = ''
        else:
            faDic[ids] += line

seq = faDic[ids]
kmerCount(seq)
for comb in itertools.product('ACGT', repeat=4):
    kmer = ''.join(comb)
    print(kmerDic.get(kmer, 0), end=' ')
    