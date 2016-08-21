def solve(num):
    if num == 0:
        return 'INSOMNIA'
    k = num
    seen = {dig:False for dig in map(str, range(10))}
    seenCount = 0
    while True:
        for dig in str(k):
            if not seen[dig]:
                seen[dig] = True
                seenCount += 1
                if seenCount == 10:
                    return k
        k += num

IN = 'A-large.in'
OUT = 'A-large.out'

nums = map(int, filter(lambda x: x, open(IN).read().split('\n')))[1:]
l = len(nums)
for i, num in enumerate(nums):
    if i % 10 == 0:
        print 'On %d of %d' % (i + 1, l)
    print >>open(OUT, 'a'), 'Case #%d: %s' % (i + 1, solve(num))

