t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input()
    count = 0
    while len(s):
        if count%2 == 0:
            if s[-1] == '-':
                while len(s) and s[-1] == '-':
                    s = s[:-1]
                count = count + 1
            else:
                while len(s) and s[-1] == '+':
                    s = s[:-1]
        else:
            if s[-1] == '+':
                while len(s) and s[-1] == '+':
                    s = s[:-1]
                count = count + 1
            else:
                while len(s) and s[-1] == '-':
                    s = s[:-1]
    print "Case #{}: {}".format(i, count)