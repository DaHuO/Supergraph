t=int(input())
s=1
while s<=t:
    n=int(input())
    l=[]
    for i in range(2*n-1):
        k=input().split()
        k=[int(k[j]) for j in range(n)]
        l.append(k)
    ele=[]
    for i in range(2*n-1):
        for j in range(n):
            if l[i][j] in ele:
                ele.remove(l[i][j])
            else:
                ele.append(l[i][j])
    ele.sort()
    ele=' '.join([str(ele[i]) for i in range(len(ele))])
    print('Case #',s,': ',ele,sep='')
    s+=1
