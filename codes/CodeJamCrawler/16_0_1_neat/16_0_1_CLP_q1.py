from itertools import count
with open('input.large') as f:
    lines = map(lambda s: int(s.strip()), f.readlines()[1:])
for x, y in enumerate(lines, 1):
    unseen = set(range(0, 10))
    if y == 0:
        print "Case #{}: INSOMNIA".format(x)
        continue
    for n in count(1):
        unseen = unseen - set(map(int, str(n * y)))
        if len(unseen) == 0:
            break
    print "Case #{}: {}".format(x, n * y )
