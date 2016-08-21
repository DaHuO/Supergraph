
tests = int(input())

for t in xrange(1,tests+1):
    n = int(input())
    if n == 0:
        print "Case #{}: INSOMNIA".format(t)
        continue
    i = 1
    s = set()
    answer = n
    while len(s) < 10:
        answer = n*i
        s = s.union(set(list(str(answer))))
        i+=1
    print "Case #{}: {}".format(t, answer)
