inp = open("input.txt")
output = open("output1.txt", "w")

for _ in xrange(int(inp.readline().strip())):
    N = int(inp.readline().strip())
    if N == 0:
        output.write("Case #%d: INSOMNIA\n" % (_ + 1))
    else:
        array = [0] * 11
        count = 0
        i = 1
        while count != 10:
            string = str(i * N)
            for x in string:
                if array[int(x)] == 0:
                    array[int(x)] = 1
                    count += 1
            i += 1
        output.write("Case #%d: %d\n" % (_ + 1, N * (i-1)))
output.close()
inp.close()
