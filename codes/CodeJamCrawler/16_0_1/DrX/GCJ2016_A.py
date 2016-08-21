def f(x):
    flag = [False] * 10
    last = 0
    while True:
        cur = last + x
        last = cur
        while cur:
            flag[cur % 10] = True
            cur /= 10
        if all(flag):
            return last

for ca in xrange(input()):
    n = input()
    if n == 0:
        ans = "INSOMNIA"
    else:
        ans = f(n)
    print "Case #" + str(ca + 1) + ":", ans
