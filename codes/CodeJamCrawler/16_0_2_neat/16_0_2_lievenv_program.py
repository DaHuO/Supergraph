# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())
for case in xrange(1, t+1):
    s = raw_input()
    counter = 0
    for i in xrange(0,len(s)-1):
        if s[i] != s[i+1]:
            counter += 1
    if s[len(s)-1] == '-':
        counter += 1
    print "Case #{}: {}".format(case, counter)
