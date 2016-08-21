fp=open('B-large.in','r')
P=fp.readlines()
L=len(P)
fp.close()
fout=open('out.out','w')
for t in range(1,L):
    S=P[t][:-1]
    s='+'+S
    bad=s.count('+-')
    ans=0
    if bad!=0:
        ans=2*bad
        if S[0]=='-':
            ans-=1
    fout.write('Case #%d: %d' %(t,ans))
    fout.write('\n')
fout.close()
