def count(N):
    x = -1
    m = 1
    digits = set()
    while len(digits) < 10:
        nx = m * N
        if x == nx:
            return "INSOMNIA"
            break
        else:
            x = nx
            m += 1
        for c in str(x):
            digits.add(c)
    return x

T = int(input())
for t in range(T):
    N = int(input())
    result = "Case #" + str(t+1) + ": " + str(count(N))
    print result

#for N in range(201):
#    count(N)


