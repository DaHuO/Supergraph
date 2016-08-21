def solve(s):
    p = ' '
    count = 0
    for c in s:
        if c != p:
            count += 1
            p = c

    return count


T = int(input())

for t in range(T):
    s = str(raw_input()).strip().rstrip('+')
    print "Case #" + str(t+1) + ": " + str(solve(s))


