# codejam
def revenge(s):
    size = len(s)
    ans = 0 if s[0] == '+' else 1

    for i in range(1,size):
        if s[i] == '+':
            continue
        elif s[i] == '-' and s[i-1] == '+':
            ans += 2
    return ans
T = input()
for i in range(1,T + 1):
    s = raw_input()
    print "Case #%d: %d" % (i, revenge(s))