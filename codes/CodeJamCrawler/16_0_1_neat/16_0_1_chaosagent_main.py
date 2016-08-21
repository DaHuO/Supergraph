n = int(raw_input().strip())
for case in xrange(1, n + 1):
    base = int(raw_input().strip())
    result = None
    if base == 0:
        result = 'INSOMNIA'
    else:
        mult = 1
        digits = set()
        while True:
            digits |= set(list(str(base * mult)))
            if len(digits) == 10:
                break
            mult += 1
        result = base * mult
    print 'Case #%d: %s' % (case, str(result))
