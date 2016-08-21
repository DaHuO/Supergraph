def f(n):
    i=1
    z = set("0123456789")
    s = set()
    prev = -1
    while True:
        next = n*i
        if next == prev: break
        t = set(str(next))
        s = s.union(t)
        if s == z:
            return next
        i+=1
        prev = next
    return "INSOMNIA"

import sys
sys.stdin = open(r"C:\Users\jake\Downloads\A-large.in", 'r')
sys.stdout = open(r"C:\Users\jake\code\A.large.out", 'w')
x = int(input())
for i in range(x):
    z = int(input())
    print("Case #%d:" % (i+1), f(z))

sys.stdin.close()
sys.stdout.close()
