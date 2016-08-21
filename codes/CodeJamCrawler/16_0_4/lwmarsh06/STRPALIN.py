inp = open("input.txt")
output = open("output1.txt", "w")

for _ in xrange(int(inp.readline().strip())):
    K, C, S = map(int, (inp.readline().strip().split()))
    array = [str(i) for i in xrange(1, K+1)]
    output.write("Case #%d: %s\n" % ( (_ + 1),' '.join(array)))
output.close()
