def readFile(filename, mode="rt"):
    with open(filename, mode) as fin:
        return fin.read()

def writeFile(filename, contents, mode="wt"):
    with open(filename, mode) as fout:
        fout.write(contents)

def helper(n, l, j):
    n = n*j
    while n:
        dig = n%10
        l[dig] = True
        n /= 10
    return (False in l)

def solve(filename):
    s = readFile(filename)
    s = s.split('\n')
    t = int(s[0])
    m = ""
    for x in xrange(t):
        n = int(s[x+1])
        l = [False]*10
        if n == 0:
            m +=  "Case #%d: INSOMNIA\n"%(x+1)
        else:
            j = 1
            while helper(n, l, j):
                j += 1
            m += "Case #%d: %d\n"%(x+1, n*j)
    writeFile("solAlarge.txt", m)

solve("A-large.in")
