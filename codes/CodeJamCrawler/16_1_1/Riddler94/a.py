inp = open("A-small-attempt0.in" , 'r')
out = open("A-small-out.txt", 'w')

def addAfter(res,l):
    res_temp = []
    for i in xrange(len(res)):
        res_temp.append(res[i]+l)
    return res_temp

def addBefore(res,l):
    res_temp = []
    for i in xrange(len(res)):
        res_temp.append(l+res[i])
    return res_temp

for case in xrange(int(inp.next())):
    s = inp.next()
    res = [s[0]]
    for j in xrange(1,len(s)):
        reA = addAfter(res, s[j])
        reB = addBefore(res, s[j])
        res = reA + reB

    res.sort()
    out.write("Case #%d: %s\n" % (case+1, res[-1]))

inp.close()
out.close()
    
