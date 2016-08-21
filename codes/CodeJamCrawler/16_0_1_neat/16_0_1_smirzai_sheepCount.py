import fileinput

#inputFile = fileinput.input();

inputFile = f = open('sampleInput', 'r')
firstLine = inputFile.readline()
t = int(firstLine)
for i in range(t):
    n = int(inputFile.readline())
    if n == 0:
        print("Case #" + str(i + 1) + ": INSOMNIA")
        continue
    sum = n
    seen = [False] * 10
    nseen = 0
    found = False

    while not found:
        ts = sum
        while ts > 0:
            rest, d= divmod(ts, 10)
            if not seen[d]:
                nseen += 1
                seen[d] = True
                if nseen == 10:
                    print("Case #" + str(i + 1) + ": " + str(sum))
                    found = True
                    break
            ts = rest
        sum += n





