num = input()

for i in xrange(num):
    n = input()
    if n == 0:
        print 'Case #%i:' % (i+1), 'INSOMNIA'
        continue
    digits = set()
    j = 1
    while True:
        digits = digits | set(str(n * j))
        if len(digits) == 10:
            print 'Case #%i:' % (i+1),  n * j
            break
        j += 1

