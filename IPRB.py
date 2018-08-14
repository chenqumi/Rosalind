'''
Mendel's First Law
'''
def Mendel(k, m, n):
    '''
    k: homo domaint
    m: hete
    n: homo recessive
    '''
    total = k + m + n
    aa = (
        n/total * (n-1)/(total-1) + 
        m/total * (m-1)/(total-1) * 0.25 + 
        m/total * n/(total-1) * 0.5 +
        n/total * m/(total-1) * 0.5
    )
    #aa = (n*(n-1) + 0.25*m*(m-1) + m*n)/total*(total-1)
    return 1 - aa

print(Mendel(26, 20, 16))