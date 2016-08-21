f = [line.rstrip() for line in open('/Users/roshil/Desktop/D-small-attempt0.in')]
out = open('/Users/roshil/Desktop/out.txt','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1,testcases+1):
    [k,c,s] = [int(p) for p in f[line].split()]
    line += 1
    l = " ".join([str(q) for q in range(1,k+1)])
    print l
    out.write("Case #"+str(i)+": "+ l + "\n")
out.close()