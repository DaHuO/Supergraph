with open('B-large.in') as f:
    T = int(f.readline()[:-1])
    for i in range(T):
        S = f.readline()[:-1]
        count = 0
        while True:
            S = S.rstrip('+')
            if len(S) == 0:
                print('Case #{0}: {1}'.format(i + 1, count))
                break;
            if S[0] == '-':
                S = S[::-1].replace('+', 'a').replace('-', '+').replace('a', '-')
            else:
                S = S[:S.find('-')].replace('+', '-') + S[S.find('-'):]
            count += 1
