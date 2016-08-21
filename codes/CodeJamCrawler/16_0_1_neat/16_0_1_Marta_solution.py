T = input()
for i in range(T):
    N = input()

    # Assume the only case for INSOMNIA is N = 0
    if N == 0:
        sol = 'INSOMNIA'
    else:
        remaining = set(map(str,range(10)))
        count = 0
        while remaining:
            count += N
            for d in set(str(count))&remaining:
                remaining.remove(d)
        sol = str(count)
    print 'Case #'+str(i+1)+": " + sol
