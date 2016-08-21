
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for c in xrange(1, t + 1):
    p = raw_input()
    n = 0
    while '-' in p:
        for i in range(len(p), 0, -1):
            if p[i-1] == '-':
                t = p[0:i]
                if t[0] == '+':
                    k = 1
                    while k < len(t) and t[k] == '+':
                        k += 1
                    t = k * '-' + t[k::]
                    n += 1
                t = t[::-1]
                t = t.replace('+','*')
                t = t.replace('-','$')
                t = t.replace('*','-')
                t = t.replace('$','+')
                p = t + p[i::]
                n += 1
    print "Case #{}: {}".format(c, n)
    # check out .format's specification for more formatting options

