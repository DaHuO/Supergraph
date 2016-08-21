t = int(input()) 
testcase = set([0,1,2,3,4,5,6,7,8,9])
for i in range(1, t + 1):
    v = set()
    n = int(input())
    if n == 0:
        print("Case #{}: INSOMNIA".format(i))
        continue
    p = str(n)
    v = v.union(set([int(s) for s in list(p)]))
    mul = 1
    while v != testcase:
        mul += 1
        p = str(n * mul)
        v = v.union(set([int(s) for s in list(p)])) 
    print("Case #{}: {}".format(i, n * mul))

    