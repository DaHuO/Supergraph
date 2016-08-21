# -*- coding: utf-8 -*-

filnema = 'B-large'
fin = open('/home/ton/Desktop/ggcj/Qualification Round 2016/B/'+filnema+'.in')
fout = open('/home/ton/Desktop/ggcj/Qualification Round 2016/B/'+filnema+'.out','wb')

def check(S):
    for s in S:
        if s == '-':
            return True
    return False

T = int(fin.readline())
for tt in range(1,T+1):
    S = fin.readline()
    ans = 0
    while check(S):
        ans += 1
        a = S.find('-')
        b = S.find('+')
        m = max(a,b)
        if m == 0:
            m = len(S)
        if S[0] == '-':
            C = '+'
        else:
            C = '-'
        S = C*m+S[m:]
    print 'Case #{0}: {1}'.format(tt,ans)
    fout.write('Case #{0}: {1}\n'.format(tt,ans))
            

fin.close()
fout.close()