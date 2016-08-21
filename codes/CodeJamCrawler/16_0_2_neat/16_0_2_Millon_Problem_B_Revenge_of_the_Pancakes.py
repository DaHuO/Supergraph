for T in range(1, int(input()) + 1):
    S = input()
    count = 0
    while True:
        if not '-' in S:
            print('Case #{0}: {1}'.format(T, count))
            break
        if S.startswith('+'):
            count += 1
            t = S.lstrip('+')
            S = '-' * (len(S) - len(t)) + t
            continue
        elif S.startswith('-'):
            count += 1
            t = S.lstrip('-')
            S = '+' * (len(S) - len(t)) + t