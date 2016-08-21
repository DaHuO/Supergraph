
f = open("b-large.in", "r")
g = open("output.txt", "wb")
line = f.readline()
line = f.readline().rstrip()
case = 1

while line:
    flips = 0
    origLine = line
    first = line[0]
    last = line[0]
    line = line[1:]
    while line:
        if (line[0] != last):
            flips += 1
            last = line[0]
        line = line[1:]

    if (last == '-'):
        flips += 1
    
    g.write('Case #{}: {}\n'.format(str(case),str(flips)))

    line = f.readline().rstrip()
    case += 1

f.close
g.close