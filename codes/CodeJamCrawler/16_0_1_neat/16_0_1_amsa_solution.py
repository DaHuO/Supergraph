def get_last_number(n):
    if n == 0:
        return 'INSOMNIA'

    multiplier = 1
    numbers = set()
    m = n
    while len(numbers) < 10:
        m = multiplier * n
        numbers.update(str(m))
        multiplier += 1
    return m

with open('./input-large.txt') as f:
    inputs = int(f.readline())
    for i in xrange(inputs):
        n = int(f.readline())
        last_number = get_last_number(n)
        print "Case #%i: %s" % (i+1, last_number)
