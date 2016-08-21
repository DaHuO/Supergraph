import math


def main():
    file = open('input.txt', 'r')
    fileOut = open('output.txt', 'w')
    cases = int(file.readline())
    for x in range(cases):
        line = lineToList(file.readline())
        print(line)
        answer = solve(line)
        for y in range(0, len(answer)):
            output = "Case #" + str(y + 1) + ": " + str(answer[y])
            print(output)
            fileOut.write(output + '\n')
    file.close()
    fileOut.close()


def solve(line):
    length = line[0]
    cases = line[1]
    solns = []
    mid = '0' * (int(length) - 2)
    base = "1" + mid + "1"
    counter = toInt(base)
    while len(solns) < int(cases):
        prime = False
        possibleSoln = []
        while isValidJamCoin(counter) is False:
            counter = counter + 1
        for x in range(2, 11):
            check = isPrime(counter, x)
            if check[0] is True:
                prime = True
                break
            else:
                possibleSoln.append(check[1])
        if prime:
            counter = counter + 1
        else:
            possible = (getBinary(counter), possibleSoln)
            solns.append(possible)
            counter = counter + 1
    return solns


def isPrime(input, base):
    # print(base)
    binary = getBinary(input)
    binList = list(binary)
    total = 0
    for x in range(0, len(binList)):
        # print(x)
        total = total + int(binList[x]) * (base ** (len(binList) - x - 1))
        # print(total)
    for x in range(2, int(math.ceil(math.sqrt(total)))):
        if total % x == 0:
            return(False, x)
    return (True, -1)


def toInt(base):
    base = "0b" + base
    base = int(base, 2)
    return(base)


def isValidJamCoin(counter):
    binary = getBinary(counter)
    if binary[0] == '1' and binary[len(binary) - 1] == '1':
        return True
    else:
        return False


def getBinary(val):
    return bin(val)[2:]


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()

if __name__ == '__main__':
    main()
