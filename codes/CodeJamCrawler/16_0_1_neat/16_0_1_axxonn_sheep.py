# [[[ for testing ]]]
# for n in range(0, 10**6+1):
#     case = n

t = int(raw_input())
for case in range(1, t+1):
    n = int(raw_input())
    if n == 0:
        print "Case #%d: INSOMNIA" % case
        continue
    seen = {}
    x = 0
    while len(seen) < 10:
        x += n
        s = str(x)
        for digit in s:
            seen[digit] = 1 # doesn't matter what this is, just that this entry exists
    print "Case #%d: %d" % (case, x)
