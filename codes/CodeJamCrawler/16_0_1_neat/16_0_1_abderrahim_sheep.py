def count(N):
    if N == 0:
        return "INSOMNIA"
    else:
        unseen = set(range(10))
        i = 0
        while unseen:
            i += 1
            unseen.difference_update(set(int(c) for c in str(i*N)))
        return i*N

T = int(input())
for i in range(T):
    N = int(input())
    print("Case #%d: %s" % (i+1, count(N)))
