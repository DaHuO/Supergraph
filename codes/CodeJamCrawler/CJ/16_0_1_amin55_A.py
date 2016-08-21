f = open("/Users/aminbarekatain/Desktop/A-large.in")
out = open("/Users/aminbarekatain/Desktop/A-large.out","w")
from numpy import array
t = int(f.readline())
for test in xrange(1,t+1):
    n = int(f.readline())
    if n == 0:
        out.write("Case #%d: INSOMNIA"%test+"\n")
        continue
    mem = array([0 for i in xrange(10)])
    k = 0
    while (mem==0).any():
        k+=1
        for i in str(k*n):
            mem[int(i)]+=1
    out.write("Case #%d: "%test+str(k*n)+"\n")
out.close()
