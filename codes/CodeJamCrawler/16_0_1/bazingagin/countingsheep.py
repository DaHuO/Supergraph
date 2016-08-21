I=int(raw_input())
l=[]
result=[]
for i in range(I):
    N=int(raw_input())
    l.append(N)
for j in range(len(l)):
    alldigit=set([])
    if l[j]!=0:
        i=1
        while len(alldigit)!=10:
            inter=l[j]*i
            digit=inter
            while (len(str(digit))!=1):
                a=digit/(10**(len(str(digit))-1))
                alldigit.add(a)
                if str(digit)[1]=='0':
                    alldigit.add(0)
                digit=int(str(digit)[1:])
            alldigit.add(digit)
            i=i+1
        result.append(str(inter))
    else:
        result.append("INSOMIA")
for s in range(len(result)):
    print "Case #%d: %s"%(s+1, result[s])