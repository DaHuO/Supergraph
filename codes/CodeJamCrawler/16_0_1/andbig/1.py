def getans(e):
    if e == 0:
        return "INSOMNIA"
        
    d=[]
    for i in range(10):
        d.append(False);
        
    cur=e
    upd(d,cur)
    while not all(d):
       cur += e
       upd(d,cur)
    
    return cur
    
def upd(d, cur):
    while cur > 0:
        d[cur % 10] = True
        cur /= 10
        
    

fileName = "A-large.in"
f = open(fileName)

l=f.readline()
l=f.readline()

inputs=[]
while l:
    inputs.append(int(l))
    l=f.readline()
    
f.close()

outfile="tst1.out"
of=open(outfile,"wb")
testCount=1

for inputEl in inputs:
    #print "Case #" + str(testCount)
    ans = getans(inputEl)
    of.write("Case #" + str(testCount) + ": " + str(ans)+'\n')
    testCount += 1

of.close()

