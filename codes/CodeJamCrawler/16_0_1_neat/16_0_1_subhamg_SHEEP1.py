inp = open("input2.txt")
output = open("output2.txt", "w")

for t in range(int(inp.readline().rstrip())):
    Number = int(inp.readline().rstrip())
    if Number == 0:
        output.write("Case #%d: INSOMNIA\n" % (t + 1))
    else:
        checker = [0] * 10
        c = 0
        i = 1
        while c != 10:
            string = str(i * Number)
            for j in range(len(string)):
                if checker[int(string[j])-1] == 0:
                    checker[int(string[j])-1] = "DONE"
                    c += 1
            i += 1
        i -= 1
        output.write("Case #%d: %d\n" % (t + 1, Number * i))
output.close()
