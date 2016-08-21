t = int(raw_input())

for case in xrange(1, t + 1):
    n = int(raw_input())

    if n == 0:
        print 'Case #%d: INSOMNIA' % case
        continue

    buck = [i for i in xrange(10)]

    number = n
    while True:
        for dig in str(number):
            dig = ord(dig) - ord('0')
            if dig in buck:
                buck.remove(dig)
        if len(buck) == 0: break
        number += n
    print 'Case #%d: %d' % (case, number)
