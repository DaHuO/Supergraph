def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


f = open('B-large.in')

count = num(f.readline())

for i in range(1, count + 1):
    s = f.readline()
    curState = None
    flip = 0
    for c in s:
        if curState is None:
            curState = c
        elif c == '+' or c == '-':
            if c != curState:
                flip += 1
                curState = c
    if curState == '-':
        flip += 1
    print 'Case #{}: {}'.format(i, flip)
