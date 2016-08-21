from __future__ import print_function


__author__ = 'Amir'


f_in = open("C:\Users\Amir\PycharmProjects\GoogleCodeJam\\files\\a\input1.txt")
f_out = open("C:\Users\Amir\PycharmProjects\GoogleCodeJam\\files\\a\output1.txt",'w')

line1 = map(int, (f_in.readline().split(" ")))
numOfCases = line1[0]


abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for n in range (numOfCases):


    print('Case #'  + str(n+1) + ': ', end = "")
    line = map(int, (f_in.readline().split(" ")))
    N = line[0]
    iterator = 0
    senList = map(int, (f_in.readline().split(" ")))
    beginSum = sum(senList)
    while (sum(senList) > 2):
        iterator +=1
        maxSenators = 0
        maxSensParty = 0
        for x in range(N):
            if (senList[x] > maxSenators):
                maxSensParty = x
                maxSenators = senList[x]

        if (beginSum%2 != 0):
            if (iterator == 1):
                print (abc[maxSensParty] + " ", end = "")
                senList[maxSensParty] -= 1
                iterator = 2
                continue

        if (iterator%2 == 0):
            print (abc[maxSensParty] + " ", end = "")
            senList[maxSensParty] -= 1
        else:
            print (abc[maxSensParty], end = "")
            senList[maxSensParty] -= 1


    for x in range(N):
        if (senList[x] != 0):
            print(abc[x], end = "")
            senList[x] -= 1



    print ("")

    #f_out.writelines('Case #'  + str(caseNum) + ': '  + 'INSOMNIA' + '\n')
