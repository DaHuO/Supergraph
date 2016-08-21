# -*- coding: utf-8 -*-

fin = open('/home/ton/Desktop/ggcj/Qualification Round 2016/A/A-large.in')
fout = open('/home/ton/Desktop/ggcj/Qualification Round 2016/A/A-large.out','wb')


T = int(fin.readline())
print 'T =',T
for tt in range(1,T+1):
    
    N = int(fin.readline())
    if N == 0:
        print 'Case #'+str(tt)+': INSOMNIA'
        fout.write('Case #'+str(tt)+': INSOMNIA\n')
    else:
        b = [True]*10     
        c = 0
        M = 0        
        while c < 10:
            M += N
            for a in str(M):
                if b[int(a)]:
                    b[int(a)] = False
                    c += 1
        print 'Case #'+str(tt)+': '+str(M)
        fout.write('Case #'+str(tt)+': '+str(M)+'\n')
fin.close()
fout.close()
