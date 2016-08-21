for tc in range(int(raw_input())):
    ansx=[]
    ansy=[]
    ans=""
    n=int(raw_input())
    a=map(int,raw_input().split())
    tt=sum(a)
    while len(ansx)+len(ansy)!=tt:
        t=a.index(max(a))
        ansx.append(t)
        a[t]-=1
        #a=[value for value in a if value != 0]
        if max(a)!=0:
            t=a.index(max(a))
            ansy.append(t)
            a[t]-=1
            #a=[value for value in a if value != 0]
    for i in range(len(ansx)):
        if len(ansy)==i:
            ans= str(unichr(ansx[i]+65)) + " "+ans
        else:
            ans+= str(unichr(ansx[i]+65))+str(unichr(ansy[i]+65))+ " "
    print "Case #"+str(tc+1)+": "+ans
