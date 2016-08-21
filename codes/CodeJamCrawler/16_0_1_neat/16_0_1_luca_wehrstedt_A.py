def run(n):
    seen = set(str(n))
    i = 1
    while True:
        i += 1
        seen |= set(str(i * n))
        if len(seen) == 10:
            return i * n

t = int(input())

for i in range(t):
    n = int(input())
    if n > 0:
        print("Case #%d: %d" % (i+1, run(n)))
    else:
        print("Case #%d: INSOMNIA" % (i+1))
