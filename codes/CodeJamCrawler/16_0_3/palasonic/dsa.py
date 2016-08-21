def rec(kol):
    global zz
    if kol==33:
        if a[32]==0:
            return
        for i in range(2,11):
            tek=0
            st=1
            u=0
            for z in range(1,33):
                tek+=a[z]*st
                st*=i
            for z in range(2,min(1000000,tek-1)):
                if (tek%z==0):
                    u=1
                    c[i]=z
                    break;
            if u==0:
                break
        if u==0:
            return
        for i in range(32,0,-1):
            print(a[i],end="")
        print('',end=" ")
        for i in range(2,11):
            print(c[i],end=" ")
        print(' ')
        zz+=1
        return
    if kol!=1:
        a[kol]=0
        rec(kol+1)
    if (zz==500):
        return
    a[kol]=1
    rec(kol+1)
    return

a=[]
c=[]
zz=0
for i in range(33):
    a.append(0)
    c.append(0)
rec(1)