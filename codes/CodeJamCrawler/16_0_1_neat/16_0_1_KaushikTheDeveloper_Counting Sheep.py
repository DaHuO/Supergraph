w=int(input())
for i in range(w):
    n=int(input())
    if n==0:
        print("Case #",end='')
        print(i+1,end='')
        print(": INSOMNIA")
        continue
    s=str(n)
    l=list(s)
    if len(l)==10:
        print("Case #",end='')
        print(i+1,end='')
        print(":",n)
    #print(n,s,l)
    for j in range(2,10**n+1):
        n1=n*j
        s1=str(n1)
        l1=list(s1)
        l=list(set(l1+l))
        #print(n1,l1,l)
        if len(l)==10:
             print("Case #",end='')
             print(i+1,end='')
             print(":",n1)
             break