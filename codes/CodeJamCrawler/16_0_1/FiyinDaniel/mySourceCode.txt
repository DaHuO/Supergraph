f1 = open('A-large.in','r')
f2 = open('myOutput.out','w')


testcases = int(f1.readline())
for j in range(testcases):
    number = int(f1.readline())
    newNumber = number
    myList = []
    def listChecker(thisList):
        if len(thisList) == 10:
            return False
        else:
            return True


    if number == 0:
        print("INSOMNIA")
        f2.write('Case #')
        f2.write(str(j+1))
        f2.write(': ')
        f2.write("INSOMNIA")
        f2.write('\n')
    else:
        while (listChecker(myList)):
            for i in range(len(str(newNumber))):
                if not int(str(newNumber)[i]) in myList:
                    myList.append(int(str(newNumber)[i]))
            newNumber += number

        print(newNumber - number)
        f2.write('Case #')
        f2.write(str(j+1))
        f2.write(': ')
        f2.write(str(newNumber - number))
        f2.write('\n')
