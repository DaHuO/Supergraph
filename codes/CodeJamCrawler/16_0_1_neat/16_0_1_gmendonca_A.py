def check_dict():
    testval = True
    return all(val==testval for val in d.values())


def check_digits(n):
    while n:
        d[str(n % 10)] = True
        n //= 10

t = int(raw_input().strip())

for x in range(1,t+1):
    n = int(raw_input().strip())
    if n == 0:
        print 'Case #%d: INSOMNIA' % x
        continue
    d = {'0' : False, '1' : False, '2' : False, '3' : False, '4' : False,
    '5' : False, '6' : False, '7' : False, '8' : False, '9' : False}
    multiplier = 0
    while not check_dict():
        multiplier += 1
        check_digits(n*multiplier)
    print 'Case #%d: %d' % (x,n*multiplier)
