inp = open("A-large.in" , 'r')
out = open("A-large-out.txt", 'w')

for case in xrange(int(inp.next())):
    num = int(inp.next())
    rset = (set(str(num)))
    if(num == 0):
        out.write("Case #%d: %s\n" % (case+1, "INSOMNIA"))
        continue
    n = 2
    num1 = 0
    tset = set('0123456789')
    while(tset != rset):
        num1 = num*n
        n += 1
        rset = rset.union(set(str(num1)))
    out.write("Case #%d: %d\n" % (case+1, num1))


inp.close()
out.close()
