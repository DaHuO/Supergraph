numInputs = int(input())
for lineNumber in range(1, numInputs + 1):
    pancakes = list(str(input())[::-1])
    pancakeIndex = 0
    blankRun = False
    flipCount = 0
    while pancakeIndex < len(pancakes):
        pancake = pancakes[pancakeIndex]
        if pancake == '+':
            if blankRun:
                flipCount += 1
                blankRun = False
            while pancake == '+':
                pancakeIndex += 1
                if pancakeIndex >= len(pancakes):
                    break
                pancake = pancakes[pancakeIndex]
                continue
        else:
            blankRun = True
            while pancake == '-':
                pancakeIndex += 1
                if pancakeIndex >= len(pancakes):
                    break
                pancake = pancakes[pancakeIndex]
            flipCount += 1
    print("Case #" + str(lineNumber) + ": " + str(flipCount))
