N = 32
J = 500

MAX_CHECKED_DIVIDER = 10 ** 6

cur = int('1' + '0' * (N - 2) + '1')

def findDivider(num):
    for i in range(2, min(num, MAX_CHECKED_DIVIDER)):
        if num % i == 0:
            return i

    return -1

jamcoins = []
proofs = []

for i in range(10 ** 10):
    binaryInter = bin(i)[2:].zfill(N - 2)
    candidate = '1' + binaryInter + '1'

    dividers = []

    for base in range(2, 11):
        curNum = int(candidate, base)
        curDiv = findDivider(curNum)

        if curDiv != -1:
            dividers.append(curDiv)
        else:
            break

    if len(dividers) == 9:
        jamcoins.append(candidate)
        proofs.append(dividers)

    if len(jamcoins) == J:
        break

if (len(jamcoins) == J):
    for i in range(len(jamcoins)):
        line = jamcoins[i]
        for j in proofs[i]:
            line += ' ' + str(j)

        print(line)
