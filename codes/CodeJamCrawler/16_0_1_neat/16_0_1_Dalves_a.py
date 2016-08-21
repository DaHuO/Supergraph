def count(n):
    digits = set()
    x = 0
    while(len(digits) < 10):
        x += n
        for d in str(x):
            digits.add(int(d))
    return x

limit = int(raw_input())

for i in xrange(limit):
    n = int(raw_input())
    print "Case #%d:" % (i+1), 
    if n == 0:
        print "INSOMNIA"
        continue
    print count(n)
