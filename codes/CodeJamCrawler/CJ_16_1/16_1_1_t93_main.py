def main():
    t = int(raw_input())
    for i in xrange(t):
        s = raw_input()
        print "Case #%d: %s" % (i+1, solve(s))

def solve(s):
    t = ''
    for c in s:
        t = best_join(t, c)
    return t

def best_join(t, c):
    for d in t:
        if d > c:
            return t + c
        elif d < c:
            return c + t
    return t + c

if __name__ == "__main__":
    main()
