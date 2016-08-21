def find_div(n):
    sq = int(n**0.5)
    for _ in xrange(2,min(10**4,sq) + 1):
        if n % _ == 0:
            return _
    return -1

t = int(raw_input())
while t > 0:
    print 'Case #1:'
    t -= 1
    n,d = map(int,raw_input().split())
    l = [0 for _ in xrange(n)]
    l[0] = 1
    l[-1] = 1
    for i in xrange(2**(n - 2)):
        temp = i
        j = 1
        while temp:
            l[j] = (temp&1)
            temp /= 2
            j += 1
        div = []
        flag = 1
        for base in xrange(2,11):
            num = 0
            for ind,bit in enumerate(l):
                if bit:
                    num += base**ind
            divi = find_div(num)
            if divi == -1:
                flag = 0
                break
            div.append(divi)
        if flag:
            s = ""
            d -= 1
            for _ in l[::-1]:
                s += repr(_)
            s += " "
            for _ in div:
                s += repr(_) + " "
            print s[:-1]
        if d == 0:
            break
