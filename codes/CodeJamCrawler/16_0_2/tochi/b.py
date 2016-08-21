def do(pancakes):
    count = 0
    minus = False
    for c in pancakes:
        if minus:
            if c == '-':
                continue
            else:
                minus = False
        else:
            if c == '-':
                minus = True
                count += 1
    r = 2 * count - 1
    return r + 1 if pancakes[0] == '+' else r

N = int(input())
for i in range(1, 1+N):
    pancakes = input()
    print('Case #%d: %s' % (i, do(pancakes)))
