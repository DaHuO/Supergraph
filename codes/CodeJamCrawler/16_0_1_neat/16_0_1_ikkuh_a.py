T = int(raw_input())

for i in range(T):
    n = int(raw_input())
    
    seen = [False for _ in range(10)]
    j = 0
    while False in seen and j*n != (j-1)*n:
        j += 1
        for c in str(n*j):
            seen[int(c)-1] = True

    if False in seen:
        print("Case #%d: INSOMNIA" % (i+1))
    else:
        print("Case #%d: %d" % (i+1, (j*n)))
