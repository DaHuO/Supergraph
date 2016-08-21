__author__ = 'pavlovick'

def stringAsBase(listNumber, base):
    baseNumber=0
    position = len(listNumber)-1
    for digit in listNumber:
        baseNumber= baseNumber+ int(digit) * (base**position)
        position = position -1
    return baseNumber

def artworksCleaning(K, C, S):
    tilesToBeCleaned=[]
    if C>K:
        C=K
    minimumAttempt = K/C
    if minimumAttempt>S:
        return 'IMPOSSIBLE'
    else:
        path=[]
        for attempt in range(0,minimumAttempt):
            tilesToBeCleaned.append(stringAsBase(range(C*attempt, C*(attempt+1)),K)+1)
        remainder = K%C
        for tiles in range(remainder, 0, -1):
            tilesToBeCleaned.append(K-tiles+1)
        return ' '.join(map(str, tilesToBeCleaned))


solution = open('solution.txt', 'w')
with open('test.txt') as f:
    N= int(f.readline())
    count = 1
    for line in f:
        inputValues = line.split()
        result = artworksCleaning(int(inputValues[0]), int(inputValues[1]), int(inputValues[2]))
        newLine = 'Case #'+ str(count) +': '+ result +'\n'
        solution.write(newLine)
        count +=1





