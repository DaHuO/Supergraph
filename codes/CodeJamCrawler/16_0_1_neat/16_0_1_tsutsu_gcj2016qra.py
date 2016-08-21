with open('A-large.in') as f:
    T = int(f.readline()[:-1])
    for i in range(T):
        s = set()
        N = int(f.readline()[:-1])
        count = 1
        while True:
            NN = count * N
            count += 1
            s |= {x for x in str(NN)}
            if len(s) == 10:
                print('Case #{0}: {1}'.format(i + 1, NN))
                break;
            elif 100000 < count:
                print('Case #{0}: {1}'.format(i + 1, 'INSOMNIA'))
                break;
