T = int(input())

def getall(l):
    ret = []
    for i in range(0, pow(10, len(l))):
        ss = '{0:0'+str(len(l))+'d}'
        s = list(ss.format(i))
        match = True
        for i,v in enumerate(l):
            if v != '?' and v != s[i]:
                match = False

        if match:
            ret.append(''.join(s))

    return ret

for t in range(T):
    a,b = input().strip().split()
    
    a = list(a)
    b = list(b)

    aa = list(map(int, getall(a)))
    ab = list(map(int, getall(b)))

    md = 99999
    val = None

    for x in aa:
        for y in ab:
            diff = abs(x-y)
            if diff < md:
                md = diff    
                val = (x,y)

    n = str(len(a))
    vs = "{0:0" + n + "d}"
    v0 = vs.format(val[0])
    v1 = vs.format(val[1])

    os = "Case #{}: {} {}".format(str(t+1), v0, v1)
    print(os)
    
