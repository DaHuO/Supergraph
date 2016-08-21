def order(n,mem):
    members=mem.split()
    sm=0
    for i in members:
        sm+=int(i)
    li=['A','B','C']
    s=''
    count=0
    non=[]
    for i in range(len(members)):
        if int(members[i])!=0:
            count+=1
            non.append(i)
        else:
            continue
    if count==2 and members[non[0]]==members[non[1]]:
        for i in range(sm/2):
            s=s+li[non[0]]+li[non[1]]+' '
        return s
    for i in range(sm-2):
        a=max(members)
        m=members.index(a)
        s=s+li[m]
        members[m]=str(int(members[m])-1)
        s+=' '
    for i in range(len(members)):
        if members[i]=='0':
            continue
        else:
            s+=li[i]
    return s
    
t = int(raw_input())
for i in range(t):
    n=int(raw_input())
    mem=raw_input().strip()
    print "Case #{}: {}".format(i+1, order(n,mem))
