def test(str):
    str+='+'
    e=len(str)-1
    k=0
    while e>0 and str[e-1]=='+' : e-=1
    for i in xrange(1,e+1):
        if str[i]!=str[i-1]:k+=1
    return k

for i in xrange(input()):
    print "Case #%d:"%(i+1),test(raw_input())
