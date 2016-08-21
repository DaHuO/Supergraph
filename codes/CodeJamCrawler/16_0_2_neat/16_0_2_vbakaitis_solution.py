import sys
cases = int(sys.stdin.readline())
for c in range(1, cases+1):
    s = sys.stdin.readline()
    l = len(s)
    y = 0
    z = "-"
    for i in range(1, l+1):
        if(s[l-i] == z):
            z = "-" if z == "+" else "+"
            y += 1
    print "Case #" + str(c) + ": " + str(y)


