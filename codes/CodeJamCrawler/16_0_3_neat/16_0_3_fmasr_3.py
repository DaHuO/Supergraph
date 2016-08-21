def getDiv(x):
    i = 3
    while i*i <= x:
        if x % i == 0:
            return i
        i = i + 1
    return None
def getRes(n,j):
    start = '1' + '0'*(n-2) + '1'
    end = '1' * n
    res = {}
    for i in range(int(start, 2), int(end, 2) + 1):
        s = ('{0:0' + str(n) +'b}').format(i)
        if s[-1] == '0':
            continue
        res_i = []
        for base in range(2,11):
            val = int(s, base)
            div = getDiv(val)
            if div == None:
                break;
            res_i.append(div)
        if len(res_i) == 9:
            res[s] = res_i
        if len(res) == j:
            return res

t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    n,j = s.split(' ')
    print("Case #{idx}: ".format(idx=i))
    res=getRes(int(n),int(j))
    for r,v in res.items():
        out = ' '.join([str(x) for x in v])
        print( r + ' ' + out )
      
