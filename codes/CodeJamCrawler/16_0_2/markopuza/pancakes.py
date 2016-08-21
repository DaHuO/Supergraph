for t in range(1, int(input()) + 1):
    p = raw_input()
    r = 0
    for i in range(1, len(p)):
        if p[i] != p[i - 1]:
            r += 1
    if p[-1] == '-':
        r += 1
    print('Case #' + str(t) +  ': ' + str(r))
