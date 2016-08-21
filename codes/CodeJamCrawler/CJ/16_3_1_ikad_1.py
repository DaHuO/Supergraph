f = open("C:\\Users\\Moulik_Adak\\Desktop\\x.in","r")
o = open("C:\\Users\\Moulik_Adak\\Desktop\\x.out","w")
t = int(f.readline())
import operator
def pr(s,tc):
    o.write("Case #"+str(tc)+": "+str(s)+"\n")
    
tc=1
m={}

while(tc!=t+1):
    n=int(f.readline())
    for i in range(n):
        m[chr(ord('A')+i)]=0
    a=f.readline().split()
    for i in range(n):
        m[chr(i+ord('A'))]+=int(a[i])
    most=-1
    secmost=-1
    mostk=-1
    secmostk=-1
    ans=""
    while(most!=0):
        most=-1
        secmost=-1
        mostk=-1
        secmostk=-1
        for k,v in m.iteritems():
            if(v>most):
                secmost=most
                secmostk=mostk
                most=v
                mostk=k
            elif(v>secmost):
                secmost=v
                secmostk=k
        if(most==0):
            break
        if(most==secmost):
            m[mostk]-=1            
            if(secmost==0):
                ans+=mostk+" "
            else:
                ans+=mostk+secmostk+" "
                m[secmostk]-=1
        else:
            if(most==1):
                m[mostk]-=1
                ap= ans[len(ans)-3:]
                ans=ans[:len(ans)-3]
                ans+=mostk+" "
                ans+=ap
            else:
                m[mostk]-=2
                ans+=mostk+mostk+" "
    pr(ans,tc)
            
            
    #pr(ans,tc)
    tc+=1
o.close()
