def main():
    caseCount = int(input())
    for caseNum in range(1, caseCount + 1):
        n = int(input())
        result = countSheep(n)
        print('Case #{caseNum}: {result}'.format(caseNum=caseNum, result=result))

def countSheep(num):
    if num == 0:
        return 'INSOMNIA'
    foundDigits = set()
    mult = 1
    while len(foundDigits) < 10:
        for digit in list(str(mult * num)):
            foundDigits.add(digit)
        mult += 1
    return (mult - 1) * num

main()