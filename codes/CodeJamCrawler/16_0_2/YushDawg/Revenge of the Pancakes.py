numCases = int(raw_input())
testCases = []
flipped = 0

def flip(S):
    global flipped
    if S.find('-') == -1:
        return

    if S[-1] == '+':
        newS = S[::-1]
        #print(S)
        #print S[:(-1 * newS.find('-'))]
        flip(S[:(-1 * newS.find('-'))])
        
    else: 
        if S[0] == '-':
            beginNeg = S.find('+')
            if beginNeg == -1:
                flipped += 1
                return
            elif beginNeg != 0:
                flipped += 1
                #print "In -"
                #print ('+' * beginNeg) + S[beginNeg:]
                flip(('+' * beginNeg) + S[beginNeg:])

        elif S[0] == '+':
            beginPos = S.find('-')
            if beginPos != 0:
                flipped += 1
                #print "In +"
                #print(('-' * beginPos) + S[beginPos:])
                flip(('-' * beginPos) + S[beginPos:])

for i in range(numCases):
    testCases.append(raw_input())

for num in range(numCases):
    flipped = 0
    S = testCases[num]
    flip(S)
    print("Case #" + str(num + 1) + ": " + str(flipped))



