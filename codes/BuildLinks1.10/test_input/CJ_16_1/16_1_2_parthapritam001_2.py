from sys import stdin as sin
t=int(sin.readline().rstrip())
for i in range(t):
    n=int(sin.readline().rstrip())
    list=[]
    count=dict()
    for j in range(2*n-1):
        l=[int(x) for x in sin.readline().rstrip().split()]
        list.append(l)
        for k in l:
            if str(k) not in count:
                count[str(k)]=1
            else:
                count[str(k)]+=1
    #now process the input
    #print(count)
    temp = []
    for item,data in count.items():
        if data%2==1:
            temp.append(int(item))
    #print(temp)
    temp.sort()
    t=[]
    for j in temp:
        t.append(str(j))
    stemp=" ".join(t)
    print("case #" + str(i+1) + ": " +stemp )
    #list.sort()
