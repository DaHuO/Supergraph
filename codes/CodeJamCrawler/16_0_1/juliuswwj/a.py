import sys


for q in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    r = "INSOMNIA"

    kk = set()
    for i in range(1, 100):
        z = str(n*i)
        for ch in z:
            kk.add(ch)
        if len(kk) == 10:
            r = n*i
            break
    
    print "Case #%d: %s" % (q+1, r)
