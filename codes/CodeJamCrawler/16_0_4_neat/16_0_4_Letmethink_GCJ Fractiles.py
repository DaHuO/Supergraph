import math

def convertToBinary(n:int):
    return int(bin(n)[2:])

file = open('D-small-attempt2.in', 'r')
myList = file.readlines()
for count in range(len(myList)):
    myList[count] = myList[count].replace('\n', '')

inputs = int(myList[0])
myList.pop(0)

for count in range(len(myList)):
    myList[count] = myList[count].split()

print(myList)

fout = open('output.out', 'w')
for count in range(inputs):
    starting = int(myList[count][0])
    iterations = int(myList[count][1])
    jobs = int(myList[count][2])
    base = ''
    
    endPositions = []
    startPositions = []
    position = []
    positions = int(math.pow(2, int(starting)))
    #print(positions)
    dropper = 0
    shift = 0
    if iterations > 1:
        while positions > 1:
            positions *= 1/4
            position.append(starting*(dropper+1)-shift)
            dropper += 1
            shift += 1
    else:
        for i in range(starting):
            position.append(i+1)
    '''
    for i in range(int(math.pow(2, int(starting)))):
        position = []
        #print(i)
        #binary = convertToBinary(i)
        #print(binary)
        for n in range(starting):
            position.append((i+1)%math.pow(2, int(n)) == (i+1)%math.pow(2, int(n+1)))
        #print(position)
        startPositions.append(position)

    #print(startPositions)
    print('here')
    count2 = 0
    for item in startPositions:
        #print(item)
        #print(iterations)
        if iterations > 1:
            for c in range(iterations-1):     
                newPosition = []
                for b in item:
                    if not b:
                        for s in startPositions[count2]:
                            newPosition.append(s)
                    else:
                        for s in range(starting):
                            newPosition.append(b)
                item = newPosition
        endPositions.append(item)
        count2 += 1

    #print(endPositions)
    end = endPositions
    choices = []
    while len(end) > 1:
        maximum = 0
        chosen = 0
        for count3 in range(len(end[0])):
            currmax = 0
            for item in end:
                if item[count3]:
                    currmax += 1
            if currmax > maximum:
                maximum = currmax
                chosen = count3

        #print(chosen)
        #print(end)
        newEnd = end
        end = []
        for count4 in range(len(newEnd)):
            if not newEnd[count4][chosen]:
                end.append(newEnd[count4])
        choices.append(chosen)

    #print(end)
    #print(choices)
    '''
    choices = position
    if len(choices) > jobs:
        base = "IMPOSSIBLE"
    else:
        base = str(choices[0])
        for i in range(len(choices)-1):
            base += ' ' + str(choices[i+1])
    output = 'Case #' + str(count+1) + ': ' + base
    print(output)
    fout.write(output + '\n')
#file.close()
fout.close()
