
T = int(input())

for ttt in range(T):
    N = int(input())
    num_seen = 0
    seen = [0]*10
    if N == 0:
        print("Case #%d: INSOMNIA" % (ttt+1))
        continue
    
    incr = N
    while 1:
        arr = [int(c) for c in str(N)]
        for i in arr:
            if seen[i] == 0:
                seen[i] = 1
                num_seen += 1
        if  num_seen == 10:
            break
        N += incr
    
    print("Case #%d: %d" % (ttt+1, N))
