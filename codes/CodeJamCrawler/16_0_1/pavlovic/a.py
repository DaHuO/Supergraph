import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    sys.stdout.write("Case #%d: " % (i + 1))    
    n = int(sys.stdin.readline().strip())
    if n == 0:
        sys.stdout.write("INSOMNIA\n")
        continue
    digit = [False] * 10
    p = 1
    while True:
        k = n * p
        while k > 0:
            digit[k % 10] = True
            k = k / 10
        over = True
        for j in range(10):
            if digit[j] == False:
                over = False
        if over:
            sys.stdout.write("%d\n" % (n * p))
            break
        p += 1

