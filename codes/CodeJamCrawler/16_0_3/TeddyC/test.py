# f = open('A-large-practice.in')
f = open('test.in')

import sys
sys.stdout = open('out', 'w')


def getDivisor(a):
#     print "a", a
    if a % 2 == 0:
        return 2
    div = 3
    while div < int(a**0.5)+1:
        if a % div == 0:
            return div
        div += 2
        if div >= 100000:
            break
    return 0

def checkJam(str):
#     print 'b', str
    res = []
    for i in xrange(2,11):
#         print str, int(str,i)
        d = getDivisor(int(str,i))
        if d==0:
            return False
        res.append(d) 
    return res
    
T = f.readline()
print "Case #1:"
l = f.readline().split()

# generate all the possible coinjams
jams = []
max = ""
c=0
for i in range(int(l[0])-2):
    max+= '1'
binmax = int(max,2)
i=0
while i <= binmax:
    s = bin(i)[2:]
    for j in range(len(max)-len(s)):
        s='0'+s
    result = checkJam('1'+s+'1')
    if result:
        c += 1
        print '1'+s+'1', ' '.join(str(x) for x in result)
    if c >= int(l[1]):
        break
    i+=1
    
    
    
