T = int(raw_input())


for i in xrange(T):
    b = [False for _ in range(10)]
    done = all(b)

    NN = int(raw_input())
    N = NN

    if N == 0:
        print "Case #" + str(i+1) + ": INSOMNIA"
        continue

    while not all(b):
        for n in str(N):
            b[int(n)] = True
        N += NN 

    N -= NN
    print "Case #" + str(i+1) + ": " + str(N)
