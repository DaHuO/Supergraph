import sys

fp = file(sys.argv[1])
t = int(fp.next())

of = file('out.txt', 'w+')

def good(s):
    return "0" in s and "1" in s and "2" in s and "3" in s and "4" in s and "5" in s and "6" in s and "7" in s and "8" in s and "9" in s

for i in range(t):
    n = int(fp.next().strip())
    s = ""
    if n == 0:
        of.write("Case #%d: INSOMNIA\n" % (i + 1))
    else:
        j = 1
        while not good(s):
            s += str(n * j)
            j += 1
        of.write("Case #%d: %d\n" % (i + 1, n * (j - 1)))

of.close()
