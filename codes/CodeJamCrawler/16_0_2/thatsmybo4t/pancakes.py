def invert_signal(signal):
    if signal == "+": return "-"
    return "+"

def invert(s):
    return map(invert_signal,s[::-1])

def last_positive(s):
    for i in xrange(len(s)-1, -1, -1):
        if s[i] == "+": return i
    return -1

def solve():
    s = raw_input()
    counter = 0
    s = list(s)
    while len(s) > 0:
        if s[-1] == "+":
            s.pop()
            continue
        elif len(s) == 1:
            counter += 1
            s.pop()
        elif s[0] == "-":
            counter += 1
            s = invert(s)
        else:
            lp = last_positive(s)
            s1 = s[:lp+1]
            s2 = s[lp+1:]
            counter += 1
            s = invert(s1) + s2
    return counter

def main():
    t = input()
    for i in xrange(1,t+1):
        ans = solve()
	print "Case #%d: %d" % (i,ans)

if __name__ == "__main__":
    main()
