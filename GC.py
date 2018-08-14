'''
Computing GC Content
'''
import sys


def calcGC(seq):
    d = {}
    totalBase = 0
    for base in seq:
        d[base] = d.get(base, 0) + 1
        totalBase += 1
    return (d['C']+d['G'])/totalBase*100


fa = sys.argv[1]
seq_dict = {}
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            seq_dict[ids] = ''
        else:
            seq_dict[ids] += line


maxID = ''
maxGC = 0.0
for ids, seq in seq_dict.items():
    gcContent = calcGC(seq)
    if gcContent > maxGC:
        maxID = ids
        maxGC = gcContent
print(maxID)
print(maxGC)
# for ids, seq in seq_dict.items():
#     gcContent = calcGC(seq)
#     print(f'{ids}\t{gcContent}')