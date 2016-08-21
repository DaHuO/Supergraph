def read_input():
    return map(lambda c: 1 if c == '-' else 0, raw_input())
    

def print_output(i, output):
    print "Case #%i: %s" % (i+1, output)

def solve(i, s):
    r = [[0,0] for i in xrange(len(s))]
    r[0][0] = 1 if s[0] == 1 else 0
    r[0][1] = 1 if s[0] == 0 else 0
    for i in xrange(1, len(s)):
        if s[i] == s[i-1]:
	    r[i][0] = r[i-1][0]
	    r[i][1] = r[i-1][1]
	    continue
	r[i][s[i]] = r[i-1][s[i]]
	r[i][1-s[i]] = r[i-1][s[i]] + 1
    return r[-1][0] 

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(t):
        input = read_input()
        output = solve(i, input)
        print_output(i, output)

