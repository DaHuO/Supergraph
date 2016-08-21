f = open('C:\! GOOGLE CODE JAM\B\B-large.in', 'r')
l = [line.strip() for line in f]
n=int(l[0])
for i in range(n):
        a,schet=l[i+1],0
        while a.rfind('-')>-1:
                if (a[0]=='+' and a.rfind('-',1)>-1
                and a.find('+',0, a.rfind('-',0))>-1):
                        inv=a[0:a.find('-')]
                        inv=inv[::-1]
                        inv=inv.replace('-','p')
                        inv=inv.replace('+','-')
                        inv=inv.replace('p','+')
                        a=inv+a[a.find('-'):]
                else:
                        inv=a[0:a.rfind('-')+1]
                        inv=inv[::-1]
                        inv=inv.replace('-','p')
                        inv=inv.replace('+','-')
                        inv=inv.replace('p','+')
                        a=inv+a[a.rfind('-')+1:]
                schet+=1
                print(schet)
        with open ('C:\! GOOGLE CODE JAM\B\B.out', 'a')as ouf:
                sss='Case #'+str(i+1)+': '+str(schet)+'\n'
                ouf.write(sss)
                ouf.close()
f.close()
