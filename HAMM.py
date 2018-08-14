'''
Counting Point Mutations
'''
import sys


def Dham(seq1, seq2):
    dh = 0
    for idx, base in enumerate(seq1):
        if base != seq2[idx]:
            dh += 1
    return dh


seq1, seq2 = sys.argv[1:3]
print(Dham(seq1, seq2))