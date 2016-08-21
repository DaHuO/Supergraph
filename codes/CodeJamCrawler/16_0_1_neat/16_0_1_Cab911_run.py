
def doit():
    num = int(raw_input())
    cnt = 1
    s = '0123456789'
    slen = len(s)
    im = 0
    while (s):
        n = num * cnt
        for i in str(n):
            s = s.replace(i, "")
        cnt = cnt + 1
        if len(s) == slen:
            im = im + 1
        else:
            im = 0
        if (im > 10000):
            return "INSOMNIA"
        slen = len(s)

    return str(n)

n = int(raw_input())
for i in range(0, n):
    print "Case #%d: %s" %(i+1, doit())
