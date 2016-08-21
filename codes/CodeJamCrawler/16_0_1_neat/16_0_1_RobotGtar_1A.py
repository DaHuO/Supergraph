def readLine(): return int(raw_input())

T = readLine()

for t in range(T):

    N = readLine()

    if N == 0:
        print 'Case #%i:' % (t + 1), 'INSOMNIA'
        continue

    results = [0]*10

    for n in range(1, 201):
        num = N*n

        while num:
            results[num%10] = 1
            num //= 10

        if sum(results) == 10:
            print 'Case #%i:' % (t + 1), n * N
            break

