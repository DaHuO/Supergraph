t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print("Case #"+str(i+1)+": INSOMNIA")
        continue
    L = set()
    c = 1
    while(len(L) != 10):
        N = str(c*n)
        for p in N:
            L.add(p)
        c += 1
    print("Case #"+str(i+1)+": "+str((c-1)*n))
