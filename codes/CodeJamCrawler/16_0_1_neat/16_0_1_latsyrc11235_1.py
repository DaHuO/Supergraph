f = [line.rstrip() for line in open('/Users/roshil/Desktop/in.txt')]
out = open('/Users/roshil/Desktop/out.txt','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1,testcases+1):
    n = f[line]
    step = f[line]
    line += 1
    l = set(n)
    j = 2
    while len(l) < 10 and n != "0":
        n = str(j*int(step))
        j += 1
        l = l.union(set(n))
    if n =="0":
        n = "INSOMNIA"
    print n
    ans = n
    out.write("Case #"+str(i)+": "+ str(n) + "\n")
out.close()