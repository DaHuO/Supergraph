IN = open("in", 'r')
OUT = open("out", 'w+')

n = IN.readline()

for x in xrange(0, int(n)):
    line = IN.readline().rstrip()
    ans = 0
    prevChar = line[0]
    for ch in line:
        if prevChar != ch:
            prevChar = ch
            ans += 1
    if prevChar == '-':
        ans += 1
    outline = "Case #" + str(x+1) + ": " + str(ans) + "\n"
    OUT.write(outline)


# Close opended files
IN.close()
OUT.close()
