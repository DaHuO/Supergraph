n=input()
ans=""
for p in range(1,n+1):
    t=input()
    l={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    if t==0:
        ans+=("Case #"+str(p)+": "+"INSOMNIA"+'\n')
    else:
        i=1
        while l['0']==0 or l['1']==0 or l['2']==0 or l['3']==0 or l['4']==0 or l['5']==0 or l['6']==0 or l['7']==0 or l['8']==0 or l['9']==0:
            k=i*t
            for j in str(k):
                l[j]+=1
            i+=1
        ans+=('Case #'+str(p)+': '+str(t*(i-1))+'\n')
print ans
