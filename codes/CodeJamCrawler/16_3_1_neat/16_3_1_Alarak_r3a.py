import sys

fhIn  = open('input_small', 'r')
fhOut = open('output', 'w') 

nCase = int(fhIn.readline())
for iCase in range(1, nCase+1):

    nParty = int(fhIn.readline())

    arrNumber   = map(lambda x: int(x), fhIn.readline().split(' '))
    arrIndex    = sorted(range(len(arrNumber)), key=lambda k: arrNumber[k], reverse=True)
    totalNumber = sum(arrNumber)

    arrResult = list()
    while totalNumber > 0:

        print('Num: ' + str(arrNumber))
        print('Idx: ' + str(arrIndex))

        # Greatest - 2
        if arrNumber[arrIndex[0]] >= 2:

            if arrNumber[arrIndex[1]] < 0.5*(totalNumber-2):

                arrResult.append(chr(ord('A') + arrIndex[0]) + chr(ord('A') + arrIndex[0]))
                arrNumber[arrIndex[0]] = arrNumber[arrIndex[0]] - 2
                totalNumber  = totalNumber - 2

                if arrNumber[arrIndex[1]] > arrNumber[arrIndex[0]]:

                    temp = arrIndex[0]
                    arrIndex[0] = arrIndex[1]
                    arrIndex[1] = temp

                if len(arrNumber) > 2:

                    if arrNumber[arrIndex[2]] > arrNumber[arrIndex[1]]:

                        temp = arrIndex[1]
                        arrIndex[1] = arrIndex[2]
                        arrIndex[2] = temp

                continue

        # Greatest - 1
        if arrNumber[arrIndex[1]] <= 0.5*(totalNumber-1):

            arrResult.append(chr(ord('A') + arrIndex[0]))
            arrNumber[arrIndex[0]] = arrNumber[arrIndex[0]] - 1
            totalNumber  = totalNumber - 1

            if arrNumber[arrIndex[1]] > arrNumber[arrIndex[0]]:

                temp = arrIndex[0]
                arrIndex[0] = arrIndex[1]
                arrIndex[1] = temp

            if len(arrNumber) > 2:

                    if arrNumber[arrIndex[2]] > arrNumber[arrIndex[1]]:

                        temp = arrIndex[1]
                        arrIndex[1] = arrIndex[2]
                        arrIndex[2] = temp

        # Greatest - 1 & subgreatest - 1
        else:

            arrResult.append(chr(ord('A') + arrIndex[0]) + chr(ord('A') + arrIndex[1]))
            arrNumber[arrIndex[0]] = arrNumber[arrIndex[0]] - 1
            arrNumber[arrIndex[1]] = arrNumber[arrIndex[1]] - 1
            totalNumber = totalNumber - 2

            if len(arrNumber) > 2:

                if arrNumber[arrIndex[2]] > arrNumber[arrIndex[0]]:

                    temp = arrIndex[0]
                    arrIndex[0] = arrIndex[2]
                    arrIndex[2] = temp

                elif arrNumber[arrIndex[2]] > arrNumber[arrIndex[1]]:

                    temp = arrIndex[1]
                    arrIndex[1] = arrIndex[2]
                    arrIndex[2] = temp

    print('Num: ' + str(arrNumber))
    strResult = format('Case #%d: %s\n' % (iCase, reduce(lambda x, y: x + ' ' + y, arrResult)))
    print(strResult)

    fhOut.write(strResult)



fhIn.close()
fhOut.close()




