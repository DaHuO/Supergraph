#author: prasunkgupta

# outfile = open("A-small-attempt0.out","w")
outfile = open("A-large.out","w")

lookup = open("lookup","r")
data=lookup.readlines()

# with open("A-small-attempt0.in","r") as infile:
with open("A-large.in","r") as infile:
    t= int(infile.readline())
    for i in xrange(t):
        n = int(infile.readline())
        outfile.write("Case #%d: "%(i+1)+data[n])

outfile.close()

print "ok"