def parseNumber(number):
    newList = list()
    for c in str(number):
        newList.append(c)

    return newList

T = int(input())
N = list()

for i in range(0, T):
    N.append(int(input()))

for i in range(0, T):
    print("Case #" + str(i+1) + ": ", end="")
    haveSeen = list()
    lastNumber = 0

    for j in range(1, 1000):
        currentNumber = j * N[i]
        numbers = parseNumber(currentNumber)
        for k in numbers:
            if k not in haveSeen:
                haveSeen.append(k)

        lastNumber = currentNumber
        if haveSeen.__len__() == 10:
            break

    if haveSeen.__len__() < 10:
        print("INSOMNIA")
    else:
        print(lastNumber)

