f = open('A-large.in')
# f = open('test.in')
 
import sys
sys.stdout = open('out', 'w')


T = f.readline()
for case in range(int(T)):
    l = f.readline()
    r = set("0123456789")
    old = set()
    m = int(l)
    temp = 0
    while len(r) > 0: 
#         print r
        r = r - set(str(m))
        temp = m
        m += int(l)
        if m in old:
            temp = "INSOMNIA"
            break
        old.add(m)
    
    print "Case #"+str(case+1)+":", temp
    
