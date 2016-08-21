import math

ts = int(raw_input())
for t in xrange(1, ts + 1):
    N = int(raw_input())

    nums = [0] * 10
    target = [1] * 10

    res = "INSOMNIA"
    if N > 0:
        acumulative = N
        while True:
            res = str(acumulative)
            for s in res:
                n = int(s)
                nums[n] = 1
            if nums == target: break
            acumulative += N
    
    print "Case #%d: %s"% (t, res)
