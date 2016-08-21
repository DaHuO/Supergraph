


T = int(raw_input())
for t in xrange(1, T+1):
    S = raw_input()
    result = ''
    for c in S:
        if len(result) == 0:
            result += c
        elif result[0] > c:
            result += c
        else:
            result = c + result
    print('Case #%d: %s' %(t, result))



