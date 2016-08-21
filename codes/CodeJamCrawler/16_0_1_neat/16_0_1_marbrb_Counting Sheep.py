cases  = int(input())


def addDigits(number, listNum):
    for digit in str(number):
        if digit not in listNum:
            listNum.append(digit)

for case in range(1,cases+1):
    number1 = input()
    number = number1
    if int(number) == 0:
        print("Case #"+str(case)+": INSOMNIA")
        continue
    listNum = list()
    mult = 2
    while len(listNum) < 10:
        addDigits(number, listNum)
        if len(listNum) == 10:
            break
        number = int(number1) * mult
        mult += 1
    
    print("Case #" + str(case) + ": " + str(number))
