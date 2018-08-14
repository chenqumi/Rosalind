'''
#chenqumi@20180804
longest increasing subsquence
'''
import sys

file = sys.argv[1]

def LIS(arr, n):
    subSeqlen = [0] * n
    for i in range(n):
        subSeqlen[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                subSeqlen[i] = max(subSeqlen[i], subSeqlen[j]+1)
    # traceback
    m = max(subSeqlen)
    idx = subSeqlen.index(m)
    maxNum = arr[idx]
    seq = [maxNum,]
    m -= 1
    while m >= 1:
        for i in range(idx):
            if subSeqlen[i] == m and arr[i] < maxNum:
                seq.insert(0, arr[i])
                maxNum = arr[i]
                break
        m -= 1
    
    return seq


def LDS(arr, n):
    subSeqlen = [0] * n
    for i in range(n):
        subSeqlen[i] = 1
        for j in range(i):
            if arr[i] < arr[j]:
                subSeqlen[i] = max(subSeqlen[i], subSeqlen[j]+1)
    # traceback
    m = max(subSeqlen)
    idx = subSeqlen.index(m)
    minNum = arr[idx]
    seq = [minNum,]
    m -= 1
    while m >= 1:
        for i in range(idx):
            if subSeqlen[i] == m and arr[i] > minNum:
                seq.insert(0, arr[i])
                minNum = arr[i]
                break
        m -= 1
    
    return seq


# l = [8, 2, 1, 6, 5, 7, 4, 3, 9]
#     [1, 1, 1, 2, 2, 3, 2, 2, 4]
# s = [35, 36, 39, 3, 15, 27, 6, 42]
#     [1,   2,  3, 1,  2,  3, 2,  4]
# t = [5, 1, 4, 2, 3]
#     [1, 1, 2, 2, 3]
n = 0
seq = ''
with open(file) as fd:
    for line in fd:
        n = line.strip()
        n = int(n)
        seq = fd.readline().strip()
l = [int(i) for i in seq.split()]


tmp1 = [str(i) for i in LIS(l, n)]
tmp2 = [str(i) for i in LDS(l, n)]
print(' '.join(tmp1))
print(' '.join(tmp2))
