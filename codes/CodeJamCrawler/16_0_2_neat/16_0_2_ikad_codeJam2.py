f = open("C:\Users\ikad\Desktop\in.txt","r")
out = open("C:\Users\ikad\Desktop\out2.txt","w")
i=0
for x in f:
    x=x.strip('\n')
    if i == 0:
        tc=x
        i+=1
        continue
    print x
    res =0
    print x[-1:]
    if x[-1:]=='-':
        res+=1
    prev = x[0]
    for j in range(0,len(x)-1):
        if x[j] != x[j+1]:
            #print prev,x[j]
            res+=1
        #prev=x[j]
    print res
    out.write("Case #"+str(i)+": "+str(res)+"\n")
    i+=1
f.close()
out.close()
