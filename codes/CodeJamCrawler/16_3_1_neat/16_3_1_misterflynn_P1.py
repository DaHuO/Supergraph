from array import *

def findMaxIndex(senators):
    max = senators[0]
    index = 0

    for i in range(0, len(senators)):
        if senators[i] > max:
            max = senators[i]
            index = i

    return index

def GetSenatorsRemaining(senators):
    count = 0

    for i in range(0, len(senators)):
        if senators[i] > 0:
            count += 1

    return count

def GetEvacuationList(senators):
    output = ""

    while 1:
        numSenators = GetSenatorsRemaining(senators)

        if numSenators > 2:
            index = findMaxIndex(senators)
            senators[index] -= 1
            output += chr(65 + index) + " "

        elif numSenators > 0:
            index1 = findMaxIndex(senators)
            senators[index1] -= 1
            index2 = findMaxIndex(senators)
            senators[index2] -= 1
            output += chr(65 + index1) + chr(65 + index2) + " "
        else:
            break

    return output




numTests = int(raw_input())
for i in range(1, numTests + 1):
    numParties = int(raw_input())
    numSenatorsPerParty = [int(x) for x in raw_input().split(" ")]

    evacuationPlan = GetEvacuationList(numSenatorsPerParty)
    str = ""
    for j in range(0, len(evacuationPlan)):
            str += (evacuationPlan[j])
    print("Case #{}: {}".format(i, str))
