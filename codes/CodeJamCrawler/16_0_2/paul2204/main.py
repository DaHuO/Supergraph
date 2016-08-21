import string

def func(s):
    if s == "":
        return 0
    else:
        length = len(s)
        for i in range(length-1, -1, -1):
            if s[i] == '+':
                return func(s[:i])
            else:
                if i == 0:
                    return 1
                else:
                    if s[i-1] == '+':
                        return func(s[:i])+2
                    else:
                        return func(s[:i])

t = int(raw_input())
for i in xrange(1, t + 1):
    m = raw_input().strip()
    result = func(m)
    print "Case #{}: {}".format(i, result)
