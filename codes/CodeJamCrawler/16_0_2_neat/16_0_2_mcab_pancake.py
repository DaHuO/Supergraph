def swap(s, pos):
    stk = list(s)
    for _ in xrange(pos):
        if stk[_] == "-":
            stk[_] = "+"
        else:
            stk[_] = "-"
    return ''.join(stk)

def main():
    caseCounter = 1
    outFile = open('pancakeout.txt', 'w')
    with open('pancakein.txt') as f:
        cases = int(next(f))
        for case in f:
            stack = case.rstrip()
            flips = 0

            while "-" in stack:
                reversedStack = stack[::-1]
                for x in xrange(len(reversedStack)):
                    if reversedStack[x] == "-":
                        stack = swap(stack, len(stack) - x)
                        flips += 1
                        break

            outFile.write('Case #' + str(caseCounter) + ': ' + str(flips) + '\n')
            caseCounter += 1
    outFile.close()

if __name__ == "__main__":
    main()