T = int(input())

def digits(n):
    while n > 0:
        yield n % 10
        n = n // 10

for t in range(T):
    n = int(input())

    if n == 0:
        print("Case #%s: INSOMNIA" % (t+1))
        continue

    digits_seen = set()

    s = n
    while len(digits_seen) != 10:
        for d in digits(s):
            digits_seen.add(d)
        s += n

    print("Case #%s: %s" % (t+1, s - n))
