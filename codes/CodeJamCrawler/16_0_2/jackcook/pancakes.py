import sys

fp = file(sys.argv[1])
t = int(fp.next())

of = file('out.txt', 'w+')

def good(s):
    return not "-" in s

def flipall(s):
    return s.replace("-", "*").replace("+", "-").replace("*", "+")

def flip(s):
    j = s.rfind("-")
    s = flipall(s[0:j+1]) + s[j+1:len(s)]
    return s

for i in range(t):
    s = fp.next().strip()
    ss = s
    j = 0

    while not good(ss):
        ss = flip(ss)
        j += 1

    of.write("Case #%d: %d\n" % (i + 1, j))

of.close()
