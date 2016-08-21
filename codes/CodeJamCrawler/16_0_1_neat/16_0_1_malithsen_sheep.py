t = int(raw_input())
inputs = []

for x in range(t):
    inputs.append(int(raw_input()))

for t, n in enumerate(inputs):
    insomnia = True
    lst = []
    for num in str(n):
        if num not in lst:
            lst.append(num)
            lst.sort()
    for y in xrange(1, 1000):
        z = n*y
        # print lst
        # print z
        if lst == [str(x) for x in range(10)]:
            insomnia = False
            print "Case #%r: %r" % (int(t)+1, n*(y-1))
            break
        for num in str(z):
            if num not in lst:
                lst.append(num)
                lst.sort()
    if insomnia:
        print "Case #%r: INSOMNIA" % (int(t)+1)
