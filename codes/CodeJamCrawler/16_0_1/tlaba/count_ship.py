def get_digits(n):
    result = set()
    i = n
    while i >= 10:
        result.add(i % 10)
        i /= 10
    result.add(i)
    return result

def get_sleep_number(n):
    if n == 0:
        return 'INSOMNIA'

    digits = set()
    i = 1
    k = n
    while len(digits) != 10:
        k = i * n
        digits = digits.union(get_digits(k))
        i += 1
    return k

f = open('data\A-large.in')
tc = int(f.readline())
print tc

for i in range(0, tc):
    n = int(f.readline())
    print "Case #%d: %s" % (i + 1, get_sleep_number(n))








