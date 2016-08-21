
maxN = 1000000
maxTry = 10000


def digitset(n):
    return set(map(int, str(n)))

def calc(i):
    seen = set()
    num = i
    found = False
    for j in xrange(maxTry):
        seen |= digitset(num)
        if len(seen) == 10:
            found = num
            break
        num += i

    return found


Tn = input()
for Tc in xrange(1, Tn + 1):
    ans = calc(input())
    if ans is False:
        ans = 'INSOMNIA'

    print 'Case #%d:' % Tc,
    print ans

