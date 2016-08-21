def solve(n):
    if n == 0:
        return "INSOMNIA"
    digits = set(range(10))
    product = 0
    while len(digits) > 0:
        product += n
        for d in str(product):
            try:
                digits.remove(int(d))
            except:
                pass
    return product

tests = int(raw_input())
for i in xrange(tests):
    n = int(raw_input())
    answer = solve(n)
    print "Case #{0}: {1}".format(i + 1, answer)
