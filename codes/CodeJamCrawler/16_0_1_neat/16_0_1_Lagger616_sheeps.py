def printCases(number, case):
    print('Number of cases:' + str(number))
    for x in range(number):
        print('Case #' + str(x+1) + ': ' + str(case[x]))


def test(caseToTest):
    test.Number += 1
    y = 1
    listofdigits = [0,1,2,3,4,5,6,7,8,9]
    lista = []
    if caseToTest == 0:
        return 'Case #' + str(test.Number) + ': ' + 'INSOMNIA'
    while True:
        caseToTest2 = y * caseToTest
        caselist = []
        for digit in str(caseToTest2):
            caselist.append(int(digit))
        for digit in listofdigits:
            if digit in caselist:
                if digit not in lista:
                    lista.append(digit)

        if len(lista) == 10:
            return 'Case #' + str(test.Number) + ': ' + str(caseToTest2)
        y += 1

f = open('A-large.in', 'r')
test.Number = 0
testsNumber = int(f.readline())
casesList = []
while testsNumber > 0:
    casesList.append(int(f.readline()))
    testsNumber -= 1
f.close()

output = open('large-output.txt', 'w')

for case in range(len(casesList)):
    output.write(str(test(casesList[case])+'\n'))

output.close()
