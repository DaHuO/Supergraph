
T = int(raw_input())

def count_sheep(N):
    if N == 0:
        return "INSOMNIA"
    d = {}
    for i in range(10):
        d[i] = 0
    i = 1
    while True:
        new_N = N*i
        i+=1
        N_str = str(new_N)
        for ch in N_str:
            d[int(ch)] = 1
        count = 0
        for key in d:
            if d[key] == 0:
                break
            if count == 9:
                return new_N
            count += 1




for i in range(T):
    print 'Case #%d:' % (i+1),
    N = int(raw_input())
    res = count_sheep(N)
    print res
