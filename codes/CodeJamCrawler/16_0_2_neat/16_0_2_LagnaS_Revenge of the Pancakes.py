fi=open('inp.in','r')
fo=open('outp.in','w')

t=int(fi.readline().rstrip('\n'))
ps=''
for k in range(1,t+1):
    s=fi.readline().rstrip('\n')
    flips=0
    l=len(s)
    for i in range(1,l):
        if s[i]!=s[i-1]:
            flips+=1
    if s[0]=='+':
        if flips&1:
            flips+=1
    elif s[0]=='-':
        if (flips&1)==0:
            flips+=1
    ps+=('Case #'+str(k)+': '+str(flips)+'\n')
fo.write(ps)
fi.close()
fo.close()