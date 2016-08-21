fi=open('inp.in','r')
fo=open('outp.in','w')

t=int(fi.readline().rstrip('\n'))
s=''
for k in range(1,t+1):
    n=int(fi.readline().rstrip('\n'))
    if n==0:
        s+=('Case #'+str(k)+': INSOMNIA\n')
        continue
    dig=set([])
    t1=n
    while True:
        temp=t1
        while temp:
            dig.add(temp%10)
            temp//=10
        if len(dig)==10:
            s+=('Case #'+str(k)+': '+str(t1)+'\n')
            break
        t1+=n
fo.write(s)

fi.close()
fo.close()
