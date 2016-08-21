N = int(input())

for i in range(N):
    a = int(input())
    if a == 0:
        print("Case #{0}: INSOMNIA".format(i + 1))
        continue
    z = a
    k=set()
    while True:
        b = a
        while b != 0:
            k.add(b % 10)
            b = b // 10
    
        if len(k) == 10:
            print("Case #{0}: {1}".format(i + 1, a))
            break
        a += z


