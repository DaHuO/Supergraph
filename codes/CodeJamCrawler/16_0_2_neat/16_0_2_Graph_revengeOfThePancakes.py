f = open('pancakeTest.txt', 'r')
output = open('pancakeResults.txt', 'w+')
numOfTests = f.readline()
count = 0
for line in f:
    count += 1
    if '-' not in line:
        output.write("Case #"+str(count)+": 0\n")
    elif '+' not in line:
        output.write("Case #" + str(count) + ": 1\n")
    else:
        stack = line.strip()
        lastIdx = 0
        loopCount = 0
        while '-' in stack:
            for idx,char in enumerate(stack):
                if char == '-':
                    lastIdx = idx
            halfstack = ''
            for x in range(lastIdx+1):
                print x
                if stack[x] == '-':
                    halfstack += '+'
                else:
                    halfstack += '-'
            stack = halfstack + stack[lastIdx+1:]
            loopCount += 1
        output.write("Case #" + str(count) + ": " + str(loopCount) + "\n")

        # while '-' in stack:

