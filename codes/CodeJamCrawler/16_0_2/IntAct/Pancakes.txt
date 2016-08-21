n = int(raw_input())
for i in xrange(1,n+1):
    flip = 0
    s = list(raw_input())
    length = len(s)
    for k in xrange(length):
        if s[length - 1 - k] == '-':
            flip += 1
            for j in xrange(length):
                if s[j] == '+':
                    s[j] = '-'
                elif s[j] == '-':
                    s[j] = '+'
    print('Case #' + str(i) +': ' + str(flip))
