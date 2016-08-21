f = open("B-large.in", "rb")
lines = []

for line in f:
    lines.append(line)

for i in range(1, len(lines)):
    p = lines[i]
    
    if p.find('-') == -1:
        print "Case #" + str(i) + ": 0"
    else:
        n = 0
        while p.find('-') != -1:
            if p.find('+') == -1:
                p = '+' * len(p)
            else:
                if p[0] == '-':
                    index = p.find('+')
                    p = ('+' * index) + p[index:]
                else:
                    index = p.find('-')
                    p = ('-' * index) + p[index:]
            n += 1

        print "Case #" + str(i) + ": " + str(n)
