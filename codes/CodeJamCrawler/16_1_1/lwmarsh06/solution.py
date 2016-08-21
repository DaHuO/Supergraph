inp = open("input.txt")
output = open("output.txt", "w+")

for _ in xrange(int(inp.readline().strip())):
    string = inp.readline().strip()
    last = string[0]
    for i in string[1:]:
        if ord(last[0]) <= ord(i):
            last = i + last
        else:
            last = last + i
    output.write("Case #%d: %s\n" % (_ + 1, last))
        

output.close()
