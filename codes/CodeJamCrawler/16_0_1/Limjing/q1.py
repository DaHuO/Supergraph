def solve_1(n):
    seen = [0] * 10
    if n==0:
        return "INSOMNIA"
    else:
        n_new=n
        while True:
            nlist = map(int, str(n_new))
            for i in nlist:
                seen[i] = 1
            if sum(seen)==10:
                return "".join(map(str,nlist))
            n_new=n_new+n



nCases = int(raw_input())
for i in range(nCases):
    n = int(raw_input())
    print "Case #"+str(i+1)+": "+solve_1(n)

#for i in range(1000000):
    #print solve_1(i)
