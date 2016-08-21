from sys import stdin as sin
t=int(sin.readline().rstrip())
for i in range(t):
    S=sin.readline().rstrip()
    #now process the input
    s1=""
    s2=""
    list=[]
    count=0
    #print(S)
    l=len(S)
    for it in range(0,l):
        item=S[it]
        #print(item)
        x=len(list)
        if(x==0):
            list.append(item)
            continue
        else:
            j=list[x-1]
            #print(list)
            l=len(list)
            #print(j)
            #print(l)
            for k in range(l-1,-1,-1):
                #print(len(list[k]))
                #print(list[k])
                if len(list[k])==len(j):
                    #print(list[k]+item)
                    #print(item+list[k])
                    list.append(list[k]+item)
                    list.append(item+list[k])
                    continue
                else:
                    break
    list.sort()
    length=len(list)
    print "case #" + str(i+1) + ": " + list[length-1]
    #print(list[length-1])