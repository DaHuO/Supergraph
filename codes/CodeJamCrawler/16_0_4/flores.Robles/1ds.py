IN = open("in", 'r')
OUT = open("out", 'w+')

n = IN.readline()

for x in xrange(0, int(n)):
    k, c, s =  map(int, IN.readline().strip().split(' '))
    ans = 0
    outline = "Case #" + str(x+1) + ":"
    OUT.write(outline)
    for i in xrange(1, k+1):
        data = " " + str(i)
        OUT.write(data)
    OUT.write("\n")

# Close opended files
IN.close()
OUT.close()
