t = int(input())

i = 1

def counting(n,acc):
    prev = acc
    sheeps.difference_update(set(str(acc)))
    if len(sheeps) == 0:
        return acc
    next = acc+n
    if next == prev:
        return 'INSOMNIA'
    return counting(n,next)

while i <= t:
    sheeps = set('0123456789')
    n = int(input())
    print("Case #%d: %s" % (i, str(counting(n,n))))
    i += 1
