t = int(input())
for i in range(t):
    n = int(input())
    m = {j:False for j in range(10)}
    ok = False
    cur = True
    if n == 0:
        print("Case #"+str(i+1)+":", "INSOMNIA")
        continue
    for j in range(n, n*1000, n):
        for z in m:
            if str(z) in str(j):
                m[z] = True
        cur = True
        for k in m:
            if m[k] == False:
                cur = False
        if cur:
            print("Case #"+str(i+1)+":", j)
            break
    if not cur:
        print("Case #"+str(i+1)+":", "INSOMNIA")
