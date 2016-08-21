def counting_sheep(filename):
    f=open(filename).read().split('\n')
    p=open('Output.txt','w')
    g=int(f[0])
    u=1
    for j in range(1,g+1):
        if u<= len(f):
            a=int(f[u])
            l=True
            c=1
            b=[]
            while l==True:
                if a==a*2:
                    print('Case #'+str(j)+': INSOMNIA')
                    p.write('Case #'+str(j)+': INSOMNIA'+'\n')
                    l=False
                else:
                    d=a*c
                    e=str(d)
                    for i in e:
                        if i not in b:
                            b.append(i)
                    if len(b)==10:
                        print('Case #'+str(j)+': ',d)
                        q=('#',str(j),': ')
                        p.write('Case #'+''+str(j)+': '+str(d)+'\n')
                        l=False
                c+=1
        u+=1
