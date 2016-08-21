IN = open("in", 'r')
OUT = open("out", 'w+')

t = IN.readline()

for x in xrange(0, int(t)):
    n = int(IN.readline())
    seen = []
    for line in xrange(0, 2 * n - 1):
        values = map(int, IN.readline().strip().split(' '))
        for value in values:
            if value in seen:
                seen.remove(value)
            else:
                seen.append(value)
    outline = "Case #" + str(x+1) + ": " +  " ".join(map(str,sorted(seen))) + "\n"
    OUT.write(outline)


# Close opended files
IN.close()
OUT.close()
