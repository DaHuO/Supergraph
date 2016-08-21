fp=open('A-large.in','r')
fp1=open('outp','w')
a=int(fp.readline())
for i in range(1,a+1):
    ss=set()
    n=int(fp.readline())
    if n==0:
        fp1.write('Case #'+str(i)+': INSOMNIA\n')
        continue
    j=1
    while(len(ss)!=10):
        nn=j*n
        ss=ss|set(str(nn))
        j+=1
    
    fp1.write('Case #'+str(i)+': '+str(nn)+'\n')
fp.close()
fp1.close()
