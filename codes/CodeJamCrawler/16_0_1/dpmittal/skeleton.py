inp = raw_input("Input File-\n")
out = raw_input("Output File-\n")
ifile = open(inp)
ofile = open(out,'w')
ofile.truncate()
itr = int(ifile.readline())
for i in xrange(itr):
    n = int(ifile.readline())
    nos = [0,1,2,3,4,5,6,7,8,9]
    j = 0
    t = True
    while(len(nos)>0):
        j+=1
        c = list(str(j*n))
        for z in c:
            if nos.count(int(z))>0:
                nos.remove(int(z))
        if j>10000:
            t = False
            break
    if t==True:
        c = "Case #%d: %d\n"%((i+1),j*n)
    else:
        c="Case #%d: INSOMNIA\n"%((i+1))
    ofile.write(c)
ofile.close()
ifile.close()
