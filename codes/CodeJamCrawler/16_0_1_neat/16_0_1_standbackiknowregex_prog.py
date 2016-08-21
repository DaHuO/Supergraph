def countsheep(n):
    digits_seen = []
    nums_seen = []
    num = None
    i = 1
    while True:
        num = i * n
        nums_seen.append(num)
        for c in str(num):
            if c not in digits_seen:
                digits_seen.append(c)
        if len(digits_seen) == 10:
            return num
        if num/100 in nums_seen:
            return "INSOMNIA"
        i += 1


f = open("A-large.in")

t = int(f.readline())
tcs = [int(x) for x in f.readlines()]

o = open("A-large.out", "w")
for ix, tc in enumerate(tcs):
    res = countsheep(tc)
    o.write("Case #{}: {}\n".format(ix+1, res))


