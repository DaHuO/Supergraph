def findSolution(i):
    options = set("0123456789")
    keepgoing = True
    if i == 0:
        return "INSOMNIA"
    else:
        counter = 1
        while counter < 500:
            number = set(str(counter * i))
            options = options.difference(number)
            if len(options) == 0:
                return str(counter * i)
            counter += 1
        return "INSOMNIA"
        
inp = open("A-large.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
lines = []
for i in range(cases):
    lines.append(int(inp.readline()))
for i in range(len(lines)):
    res.write("Case #" + str(i+1) + ": " + findSolution(lines[i]) + "\n")
    print(i)
