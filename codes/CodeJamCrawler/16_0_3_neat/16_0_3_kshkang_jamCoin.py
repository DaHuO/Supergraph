#make JamCoin template
#make list of possible combinations
#check each for all-base prime
import math
import itertools as tools

file = open("C-small-attempt0 (1).in")
numOfCases = int(file.readline().strip('\n'))

finalFile = open('answer.txt', 'w')


#make JamCoinTemplate
def makeTemplate(file):
    print("making template....")
    data = file.readline().strip("\n").split(" ")
    length = int(data[0])
    numOfAnswer = int(data[1])
    return length, numOfAnswer

#find Combinations
def findCombo(length):
    print("finding combo....")
    combos = list(tools.product([0,1], repeat=length))
    subtract = 0
    combos = [x if x[0] == 1 and x[len(x) - 1] == 1 else 'a' for x in combos]
    while 'a' in combos:
        combos.remove('a')


    return combos

#test Combo
def testCombo(combos, numOfAnswers):
    print("testing combo....")
    print(len(combos))
    answer = []
    onNum = 0
    for x in combos:
        onNum += 1
        print(onNum)
        if testBases(x) == True:
            if len(answer) < numOfAnswers * 2:
                answer.append(x)
                answer.append(writeBases(x))
    return answer



def writeBases(list):
    print("writingBases")
    sol = []
    list = str(''.join([str(x) for x in list]))

    for x in range(2, 11):
        sol.append(int(list, base = x))

    return findDivisor(sol)

def findDivisor(sol):
    print("finding Divisors")
    factorsol = []
    for x in sol:
        for num in range(2, x + 1):
            if x % (num) == 0:
                factorsol.append(num)
                break
    return factorsol



def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#test different bases
def testBases(list):
    list = str(''.join([str(x) for x in list]))

    for x in range(2,11):
        if is_prime(int(list, base = x)) == True:
            return False
    return True


#write answer with bases
def writeAnswer(list, case, answerFile):
    print("writing Answer....")
    answer = "Case #%s:\n" % (case + 1)
    for x in range(len(list) // 2):
        binary = list[0]
        binary = [str(x) for x in binary]
        binary = ''.join(binary)
        binary = int(binary)
        answer += ('%s%s\n' % (binary,toIntString(list[1])))
        list.remove(list[1])
        list.remove(list[0])
    answerFile.write(answer)


def toIntString(list):

    myString = ''
    for x in list:
        myString += (' %s' ) % int(x)

    return myString


for case in range(numOfCases):
    length, numOfAnswers = makeTemplate(file)
    combos = findCombo(length)
    answers = testCombo(combos,numOfAnswers)
    answer = writeAnswer(answers, case, finalFile)
    print(answer)

    print("next")

