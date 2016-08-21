def sleep(n):
    seen = [False]*10
    saved = n
    m = 0
    if n == 0:
        return("INSOMNIA")
    while(seen.count(True) != 10):
        m+=1
        n = saved*m
        while(n > 0):
            seen[n%10] = True
            n = int(n/10)
    return(saved*m)

T = int(input())
results = [None]*T
for j in range(T):
    results[j] = sleep(int(input()))
for i in range(T):
    print("Case #{}: {}".format(i+1, results[i]))