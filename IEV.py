'''
Calculating Expected Offspring
'''
def IEV(args):
    n1 = args[0]
    n2 = args[1]
    n3 = args[2]
    n4 = args[3] * 0.75
    n5 = args[4] * 0.5
    n6 = args[5] * 0
    prob = n1 + n2 + n3 + n4 + n5 + n6
    return prob * 2

print(IEV([18321, 16299, 18777, 19303, 17306, 16751]))