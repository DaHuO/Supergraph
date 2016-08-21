inp = raw_input("Input File-\n")
out = raw_input("Output File-\n")
ifile = open(inp)
ofile = open(out,'w')
ofile.truncate()
itr = int(ifile.readline())
for i in xrange(itr):
    n = list(ifile.readline())
    no = 0
    while(n.count('-')>0):
        k = (len(n) - 1) - n[::-1].index('-')
        for z in xrange((k+1)):
            if n[z]=='+':
                n[z]='-'
            else:
                n[z]='+'
        no+=1
    c = "Case #%d: %d\n"%((i+1),no)
    ofile.write(c)
ofile.close()
ifile.close()
