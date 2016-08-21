T = int(raw_input())


for i in range(T):
    print 'Case #%d:' % (i+1),
    cakes = raw_input()
    current = cakes[0]
    result = 0
    for i in cakes:
        if i == current:
            continue
        else:
            result += 1
            current = i
    if i == '+':
        pass
    else:
        result+=1
    print result
