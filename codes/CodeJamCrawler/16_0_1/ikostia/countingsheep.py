def read_input():
    return int(raw_input())

def print_output(i, output):
    print "Case #%i: %s" % (i+1, output)

def digits(m):
    res = []
    while m:
        res.append(m % 10)
        m = m / 10
    return res

def solve(i, n):
    if 0 == n:
         return "INSOMNIA"
    
    d = set(digits(n))
    m = n
    i = 1
    while len(d) <  10:
        m += n
	d |= set(digits(m))
        i = i + 1

    return str(m)

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(t):
        input = read_input()
        output = solve(i, input)
        print_output(i, output)

