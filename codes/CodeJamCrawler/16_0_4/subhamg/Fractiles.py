inp = open("input.txt")
output = open("output1.txt", "w")

for _ in range(int(inp.readline().strip())):
    K, C, S = map(int, (inp.readline().strip().split()))
    array = [str(i) for i in range(1, K+1)]
    output.write("Case #%d: %s\n" % ( (_ + 1),' '.join(array)))
output.close()
