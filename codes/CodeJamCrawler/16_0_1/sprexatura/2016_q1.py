f = open('input.large', 'r')
o = open('large.out', 'w')

T = int(f.readline().strip())

def fallAsleep(digits):
    if len(digits) == 10:
        return True
    return False

def solve(N):
    digits = []
    for n in xrange(1, 1000001):
        lastName = int(N)*n
        lastName = str(lastName)
        for d in lastName:
            if d not in digits:
                digits.append(d)
            if(fallAsleep(digits)):
                return lastName
    return "INSOMNIA"

for t in xrange(T):
    n = f.readline().strip()
    res = solve(n)
    s = "Case #%d: %s\n" % (t+1, res)
    #print s
    o.write(s)
