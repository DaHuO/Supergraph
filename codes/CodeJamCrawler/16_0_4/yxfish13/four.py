import random;
from math import sqrt
fp =open('b.in');
n = int(fp.readline());

for ttt in range(1,n+1):
    data = fp.readline();
    [K,C,S]=map(int,data.split(' '))
    #print K,C,S
    if (S*C<K):
        print 'Case #%d: IMPOSSIBLE'%(ttt)
    else:
        now=0
        ans = "";
        ts=0;
        while now<K:
            ts=0
            for x in range(now,now+C):
                #print now,now+C+1,x,K
                if (x<K):
                    #print x
                    ts=ts*K+x;
            ts += 1;
            ans = ans+' '+str(ts)
            now+=C;
            #print ',',now
        print 'Case #%d: %s'%(ttt,ans)
    
