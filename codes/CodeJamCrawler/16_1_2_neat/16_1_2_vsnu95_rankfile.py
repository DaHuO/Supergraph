for t in range(int(input())):
    n = int(input())
    l=[]
    ans1 = set()
    for j in range(2*n-1):
        m = list(map(int,input().split()))
        for k in m:
            l.append(k)
    for k in l:        
        if(l.count(k)%2!=0):
            ans1.add(k)

    ans = list(ans1)
    ans.sort()
    st =''
    for i in ans:
        st+= str(i) + " "    
    st = "Case #"+ str((t+1))+": " + st
    print(st)        
