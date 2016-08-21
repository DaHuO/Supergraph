
inF = open('B-large.in.txt','r')
ouF = open('MaryamQ1.out','w')
t = int(inF.readline())
for x in xrange(t):
    seq = inF.readline().strip()+'+'
    lsch = seq[0]
    count = 0
    for c in seq:
        if c != lsch:
            lsch = c
            count += 1
    ouF.write("Case #" + str(x+1) + ": " + str(count)+'\n')
inF.close()
ouF.close()
    
