#author: prasunkgupta

# outfile = open("B-small-attempt0.out","w")
outfile = open("B-large.out","w")

with open("B-large.in","r") as infile:
# with open("B-small-attempt0.in","r") as infile:
    t= int(infile.readline())
    for i in xrange(t):
        s = infile.readline().strip()
        n = s.count('+-') * 2
        if s[0] == '-':
        	n += 1
        outfile.write("Case #%d: %d\n"%((i+1), n))

outfile.close()

print "ok"