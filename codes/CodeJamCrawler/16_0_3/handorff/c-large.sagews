import itertools
x = PolynomialRing(RationalField(), 'x').gen()
count = 0
out = []
for i in xrange(1, 32):
    perms = itertools.combinations(range(1, 31), i)
    for p in perms:
        f = x^31 + 1
        for j in list(p):
            f += x^j
        if "*" in str(f.factor()):
            count += 1
            out.append(f)
        if count == 500:
            break

print "Case #1:"
for f in out[:500]:
    foo = list(f.factor())[0][0]

    print f(10), ' '.join(map(str, [foo(i) for i in range(2, 11)]))
