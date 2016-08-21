def main():
    caseCount = int(input())
    for caseNum in range(1, caseCount + 1):
        pancakes = input()
        result = calculatePancakeFlips(pancakes)
        print('Case #{caseNum}: {result}'.format(caseNum=caseNum, result=result))

def calculatePancakeFlips(pancakes):
    flips = 0
    while '-' in pancakes:
        if pancakes[0] == '+':
            firstBlank = pancakes.find('-')
            pancakes = flip(pancakes, firstBlank)
        else:
            lastBlank = pancakes.rfind('-')
            pancakes = flip(pancakes, lastBlank + 1)
        flips += 1
    return flips

def flip(pancakes, count):
    top = pancakes[:count]
    bottom = pancakes[count:]
    flippedTop = ''.join(['-' if p == '+' else '+' for p in top[::-1]])
    return flippedTop + bottom

main()
