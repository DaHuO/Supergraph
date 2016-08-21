t=open("A-large.in")
t1=open("out4.txt", "wb")

text=t.read()
intslist=text.split("\n")
le=int(intslist[0])
u=1
for u in range(1,le+1):
    k=intslist[u]
    
    if k=='0':
        t1.write("Case #{}: INSOMNIA".format(u))
        t1.write("\n")
    else:
        temp=[]
        i=0
        while len(temp)!=10:
            i=i+1
            kint=i*int(k)
            kstr=str(kint)
            for j in range(0,len(kstr),1):
                if kstr[j] not in temp:
                    temp.append(kstr[j])
        t1.write("Case #{}: {}".format(u, kstr))
        t1.write("\n")
    u=u+1
t.close()
t1.close()

