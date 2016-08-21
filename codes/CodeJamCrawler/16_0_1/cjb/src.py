def openFile():
    f = open("/Users/bosley/Downloads/A-small-attempt0.in")
    lines = [x.rstrip() for x in f.readlines()]
    n = int(lines[0])
    return n, lines

def go(n, lines):
    f = open("/Users/bosley/Desktop/A.out",'w')
    for i in range(0, n):
        m = int(lines[i+1])
        s = solve(m)
        f.write('Case #{}: {}\n'.format(i+1, s))

def getdigits(n):
    digits = []
    if n < 10:
        return [n]
    while n > 0:
        digits.append(n%10)
        n /= 10
    return digits

def solve(m):
    i = 0
    if m == 0:
        return 'INSOMNIA'
    digits = set()
    while len(digits) < 10:
        i = i + 1
        digits.update(getdigits(i*m))
        #print i, m, digits
    return i*m

n, lines = openFile()
go(n, lines)



