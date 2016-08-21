schet,d=int(input()),1
for i in range(schet):
    a=input()
    ii=1
    d=[]
    if a!='0':
        s=0
        while s==0:
            aa=int(a)*ii
            a2=str(aa)
            for iii in range(len(a2)):
                d.append(a2[iii])
            if ('1' in (d) and '2' in(d)
            and '3' in (d)and '4' in(d)
            and '5' in (d)and '6' in(d)
            and '7' in (d)and '8' in(d)
            and '9' in (d)and '0' in(d)):
                s=1
            ii+=1
            #print(d)
        print('Case #'+str(i+1)+': '+str(aa))
    else:
        print('Case #'+str(i+1)+': INSOMNIA')
    d=[]