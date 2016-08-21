t=int(raw_input())
alpha=['A','B','C']
for i in range(t+1):
    done=False
    print "Case #"+`i+1`+":",
    n=int(raw_input())
    count=0
    l=map(int,raw_input().split())
    total=0
    even=True
    for j in range(len(l)):
        total=total+l[j]
    while total>0:
        
        index1=-1
        index2=-1
        index1=l.index(max(l))
        l[index1]=l[index1]-1
        if total==3:
            even=False
        if l[index1]==0:
            count=count+1
        if even:
            index2=l.index(max(l))
            l[index2]=l[index2]-1
            if l[index2]==0:
                count=count+1
        else:
            even=True
        if index1!=-1 and index2!=-1:
            print alpha[index1]+alpha[index2],
            total=total-2
        elif index1!=-1:
            print alpha[index1],
            total=total-1
    print ""
        

