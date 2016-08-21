import collections
def solve(i):
    num=[]
    l = collections.Counter(i.lower())
    while l['z']>0:
        l=l-collections.Counter('zero')
        num.append(0)
    while l['w']>0:
        l=l-collections.Counter('two')
        num.append(2)
    while l['u']>0:
        l=l-collections.Counter('four')
        num.append(4)
    while l['x']>0:
        l=l-collections.Counter('six')
        num.append(6)
    while l['g']>0:
        l=l-collections.Counter('eight')
        num.append(8)
    while l['o']>0:
        l=l-collections.Counter('one')
        num.append(1)
    while l['h']>0:
        l=l-collections.Counter('three')
        num.append(3)
    while l['f']>0:
        l=l-collections.Counter('five')
        num.append(5)
    while l['s']>0:
        l=l-collections.Counter('seven')
        num.append(7)
    while l['n']>0:
        l=l-collections.Counter('nine')
        num.append(9)
    num.sort()
    return ''.join(map(str,num))


    

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        info = raw_input()
        print("Case #%i: %s" % (caseNr, solve(info)))
