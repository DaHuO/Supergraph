T = input()

def solve():
    n = input()
    # print n
    if n == 0:
        return 'INSOMNIA'

    digits = set([0,1,2,3,4,5,6,7,8,9])
    curr = n
    while digits:
        for c in str(curr):
            i = int(c)
            if i in digits:
                digits.remove(int(c))
        # print digits
        curr += n
    return curr-n

for t in range(T):
    ans = solve()
    print 'Case #{0}: {1}'.format(t+1, ans)
