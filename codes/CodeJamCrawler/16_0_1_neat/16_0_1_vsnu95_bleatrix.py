t = int(input())
for i in range(t):
    n = int(input())
    f = 0
    summ = 0
    a = set()
    if(n == 0):
        f=2
        print("Case #"+str(i+1)+": INSOMNIA")
    while(f==0):
        summ += n
        b = list(map(int,str(summ)))
        for x in b:
            a.add(x)
        if(len(a) == 10):
            f=1
    if(f==1):
        print("Case #"+str(i+1)+": "+str(summ))
        
    
