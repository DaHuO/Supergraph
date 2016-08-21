import sys
nl = sys.stdin.read().split()[1:]
for case,n in enumerate(nl):
    n = int(n)
    digits = [False]*10
    i = 1
    while True:
        nk = n * i
        i = i + 1 
        for d in str(nk):
            digits[int(d)] = True
        if sum(digits) == 10:
            print("Case #{}: {}".format(case+1,nk))
            break
        if i > 1000:
            print("Case #{}: INSOMNIA".format(case+1))
            break
