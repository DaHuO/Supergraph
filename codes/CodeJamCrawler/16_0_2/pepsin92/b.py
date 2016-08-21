for tc in range(1, int(input())+1):
    line = input().strip()+'+'
    res = 0
    for a, b in zip(line[:-1], line[1:]):
        if a!=b:
            res+=1

    print('Case #{}: {}'.format(tc, res))