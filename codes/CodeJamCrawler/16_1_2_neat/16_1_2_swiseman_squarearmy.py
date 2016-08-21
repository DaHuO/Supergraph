from collections import Counter

def getmissing(input):


    answer  = []
    outputanswer = ""
    parsedinput = input.split()
    parsedinput = map(int, parsedinput)
    max_number = max(parsedinput)


    for i in xrange(1, int(max_number) + 1):
        count = 0
        for l in parsedinput:
            if l == i:
                count = count + 1
        if count % 2 == 1:
            answer.append(str(i))

    outputanswer = " ".join(answer)

    return outputanswer



f = open('testcases', 'r')
g = open('output', 'w')
content = f.readlines()
numOfCases = int(content[0])
iter = 1
s = ""

testsDone = 0
currTest = 1

while testsDone < numOfCases:
    numOfSheets = int(content[iter])*2-1
    instring = ""
    for l in xrange(iter+ 1, iter + numOfSheets + 1):
        instring = instring + content[l]

    #print instring
    testsDone = testsDone + 1
    print "Case #" + str(currTest) + ": " + str(getmissing(instring))
    s = s + "Case #"+str(currTest)+": "+ str(getmissing(instring) + "\n")
    iter = iter + numOfSheets + 1
    currTest = currTest + 1
g.write(s)