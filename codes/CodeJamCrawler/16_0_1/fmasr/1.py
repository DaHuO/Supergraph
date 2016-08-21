
def getRes(n):
    if n == 0:
        return 'INSOMNIA'
    s = set()
    x = n
    while(1):
        string = str(x)
        for c in string:
            s.add(int(c))
        if len(s) == 10:
            return string
        x = x + n

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    print("Case #{idx}: {res}".format(idx=i, res=getRes(n)))
