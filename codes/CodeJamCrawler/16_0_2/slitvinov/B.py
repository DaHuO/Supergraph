import fileinput

f = fileinput.input()
nc = int(f.next())

def strip(a):
    if len(a)>0 and a[-1]=='\n':
        return a[:-1]
    else:
        return a

def inv(s):
    if s=="+":
        return "-"
    else:
        return "+"

def solve(a):
    a = a[::-1]
    skip = '+'
    ans  = 0
    for c in a:
        if c!=skip:
            ans = ans + 1
            skip = inv(skip)
    return ans

for ic in xrange(1, nc+1):
    line = f.next()
    line = strip(line)
    ans = solve(line)
    print "Case #%d: %s" % (ic, str(ans))
    
