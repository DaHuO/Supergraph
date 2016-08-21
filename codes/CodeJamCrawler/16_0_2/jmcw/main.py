
t = int(raw_input())

for i in range(t):
    print "Case #{}:".format(i+1),
    s = raw_input() + "+"
    v = 0
    for j in range(len(s)-1):
        if s[j] != s[j+1]: v += 1

    print v
