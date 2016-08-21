
# -*- coding: utf-8 -*-


filename = 'D-large'
filedir = '/home/ton/Desktop/ggcj/Qualification Round 2016/D/'
fin = open(filedir + filename + '.in')
fout = open(filedir + filename + '.out','wb')

T = int(fin.readline())
for tt in range(1,T+1):
    [K, C, S] = map(int,fin.readline().strip().split())
    ans = 'Case #'+str(tt)+':'
    if (C*S < K):
        ans += ' IMPOSSIBLE'
    else:
        r = range(K)
        i = 0
        for i in range(0,K,C):
            a = r[i:(i+C)]
            n = 0            
            for b in a:
                n *= K
                n += b
            ans += ' '+str(n+1) 

    print ans
    fout.write(ans+'\n')

fin.close()
fout.close()