case = int(input())
for z in range(1,case+1):
    n = int(input())
    d = {}
    c = 1
    if n==0:
        print("Case #"+str(z)+": INSOMNIA")
        continue
    while True:
        x = c*n
        while x > 0:
            d[x%10] = 1
            x = x//10
        if len(d.keys()) == 10:
            break
        c+=1
    print("Case #"+str(z)+":",c*n)
