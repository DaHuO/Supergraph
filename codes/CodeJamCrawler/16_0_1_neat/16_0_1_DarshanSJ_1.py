t=input()
count=1
while count<=t:
    s=set('0123456789')
    x=input()
    if x==0:
        print 'Case #'+str(count)+': INSOMNIA'
    else:
        y=0
        while len(s)!=0:
            y=y+x
            s=s-set(str(y))

        print 'Case #'+str(count)+': '+str(y)
    count+=1
