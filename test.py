'''
chenqumi@20180815
Speeding Up Motif Finding
The failure array of s is an array P of length n for which 
P[k] is the length of the longest substring s[j:k] 
that is equal to some prefix s[1:k−j+1], where j CANNOT equal 1 
(otherwise, P[k] would always equal k). By convention, P[1]=0
'''
import sys


if len(sys.argv) == 1:
    print("\nUsage: {} <> ".format(sys.argv[0]))
    sys.exit()

fa = sys.argv[1]


def kmp_preprocess(s):
    j = -1
    b = [j]

    for i, c in enumerate(s):
        while j >= 0 and s[j] != c:
            j = b[j]
        j += 1
        b.append(j)

    return b[1:]


ids = ''
faDic = {}
with open(fa) as FA:
    for line in FA:
        line = line.strip()
        if line.startswith('>'):
            ids = line.split('>')[1]
            faDic[ids] = ''
        else:
            faDic[ids] += line

seq = faDic[ids]


F_array = [0] * len(seq)
k = 0
for i in range(2, len(seq) + 1):
    while k > 0 and seq[k] != seq[i - 1]:
        k = F_array[k - 1]
    if seq[k] == seq[i - 1]:
        k += 1
    F_array[i - 1] = k

# for i in F_array:
#     print(i, end=' ')
# for i in kmp_preprocess(seq):
#     print(i, end=' ')