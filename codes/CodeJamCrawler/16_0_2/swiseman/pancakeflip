
def flipPancakes(n):

    flipCount = 0

    isAllHappy = False

    if n.find("-") == -1:
        isAllHappy = True

    while (isAllHappy == False):
        flippedStack = ""

        if n[0] == "-":
            k = n.rfind("-")
            selectedPancakes = n[0:k+1]
            reversedSelectedPancakes = selectedPancakes[::-1]
            flippedSelectedPancakes = ""
            for e in reversedSelectedPancakes:
                if e == "-":
                    flippedSelectedPancakes = flippedSelectedPancakes + "+"
                else:
                    flippedSelectedPancakes = flippedSelectedPancakes + "-"
            flippedStack = flippedSelectedPancakes + n[k+1:]


        if n[0] == "+":
            k = n.find("-")
            selectedPancakes = n[0:k]
            reversedSelectedPancakes = selectedPancakes[::-1]
            flippedSelectedPancakes = ""
            for e in reversedSelectedPancakes:
                if e == "-":
                    flippedSelectedPancakes = flippedSelectedPancakes + "+"
                else:
                    flippedSelectedPancakes = flippedSelectedPancakes + "-"
            flippedStack = flippedSelectedPancakes + n[k:]
        n = flippedStack
        flipCount = flipCount + 1

        if n.find("-") == -1:
            isAllHappy = True

    return flipCount






f = open('testcasesP', 'r')
g = open('outputP', 'w')
content = f.readlines()
numOfCases = int(content[0])
iter = 0
s = ""
for n in content:
    if iter == 0:
        pass
    else:
        print "Case #"+str(iter)+": "+ str(flipPancakes (str(n)))
        s = s + "Case #"+str(iter)+": "+ str(flipPancakes(n)) + "\n"
    iter = iter + 1
g.write(s)