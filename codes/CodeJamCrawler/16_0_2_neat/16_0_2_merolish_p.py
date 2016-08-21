for t in range(int(input())):
    s = input() + '+'
    print('Case #{}: {}'.format(t + 1, s.count('+-') + s.count('-+')))
