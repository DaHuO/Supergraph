caseCount = int(raw_input())

for caseNum in xrange(1, caseCount + 1):

    stack = [ pancake for pancake in str(raw_input()) ]
    flips = 0

    currentSymbol = stack[0]
    flippedSymbol = ''

    while True:
        currentPancake = 0
        for pancake in stack:
            if pancake == currentSymbol:
                currentPancake += 1;
            else:
                break

        if currentPancake == len(stack) and currentSymbol == "+":
            print "Case #{}: {}".format(caseNum, flips)
            break
        else:
            if currentSymbol == '+':
                flippedSymbol = '-'
            else:
                flippedSymbol = '+'

            for i in xrange(0, currentPancake):
                stack[i] = flippedSymbol

            currentSymbol = flippedSymbol
            flips += 1
