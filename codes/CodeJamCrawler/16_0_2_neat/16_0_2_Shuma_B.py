def compress(s):
    ret = s[0]
    for c in s:
        if ret[-1] == c:
            continue
        ret += c
    return ret

def solve(s):
    s = compress(s)
    if s[-1] == "+":
        s = s[:-1]
    return len(s)

for tc in xrange(1, input()+1):
    print "Case #{}: {}".format(tc, solve(raw_input()))

