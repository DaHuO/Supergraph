__author__ = 'Amir'

f_in = open("C:\Users\Amir\PycharmProjects\GoogleCodeJam\\files\\CountingSheep\input1.txt")
f_out = open("C:\Users\Amir\PycharmProjects\GoogleCodeJam\\files\\CountingSheep\output1.txt",'w')


line1 = map(int, (f_in.readline().split(" ")))
numOfCases = line1[0]
caseNum = 0

for n in range (numOfCases):
    caseNum += 1
    line = map(int, (f_in.readline().split(" ")))
    N = line[0]
    counter = 0
    digitMemory = [0 for n in range(10)]

    #for an n digit number, all digits will be reached at most when an n+1 digit number beginning with 9 will appear

    for i in range(1,100):
        currNum = i*N
        currNumStr = str(currNum)
        for m in range(10):
            if (digitMemory[m] == 0):
                if (str(m) in currNumStr):
                    digitMemory[m] = 1
                    counter += 1

        if (counter == 10):
            print 'Case #'  + str(caseNum) + ': '  + currNumStr
            f_out.writelines('Case #'  + str(caseNum) + ': '  + currNumStr + '\n')

            break

    if (counter == 1):
         print 'Case #'  + str(caseNum) + ': '  + 'INSOMNIA'
         f_out.writelines('Case #'  + str(caseNum) + ': '  + 'INSOMNIA' + '\n')




