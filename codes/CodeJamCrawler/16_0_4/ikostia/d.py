def read_input():
    return map(int, raw_input().split())

def print_output(i, output):
    print "Case #%i: %s" % (i+1, output)

def solve(i, input):
    k, c, s = input
    if c*s < k:
        return 'IMPOSSIBLE'
    if c == 1 or s == k:
        return ' '.join(map(str, range(1, k+1)))
    c -= 1
    r, ind = [], 1
    for i in xrange(s):
       d = 0
       md = k**c * ind
       for j in xrange(c+1):
           d += (ind-1) * k**(c-j)
           ind += 1
       r.append(min(d + 1, md))
       if ind > k:
           break
    return ' '.join(map(str, r))

if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(t):
        input = read_input()
        output = solve(i, input)
        print_output(i, output)

