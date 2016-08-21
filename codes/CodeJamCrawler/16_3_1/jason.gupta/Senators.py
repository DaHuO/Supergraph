def Senator():
    f = open("test.txt", 'r')
    lines = f.readlines()
    counter = 1
    for x in range(int(lines[0].strip())):
        numParties = int(lines[counter].strip())
        numList = map(int, lines[counter + 1].strip().split(" "))
        finalString = "Case #{}: ".format(x+1)
        while sum(numList) != 0:
            max = 0
            indexes = []
            for y in range(numParties):
                if numList[y] > max:
                    indexes = [y]
                    max = numList[y]
                elif numList[y] == max:
                    indexes.append(y)
            if len(indexes) == 1:
                if numList[indexes[0]] >= 2:
                    evac = str(unichr(65+indexes[0]))*2
                    finalString += evac + " "
                    numList[indexes[0]] -= 2
                else:
                    evac = str(unichr(65+indexes[0]))
                    finalString += evac + " "
                    numList[indexes[0]] -= 1
            elif len(indexes) == 3:
                evac = str(unichr(65 + indexes[0]))
                finalString += evac + " "
                numList[indexes[0]] -= 1
            elif len(indexes) >= 2:
                evac = str(unichr(65+indexes[0])) + str(unichr(65+indexes[1]))
                finalString += evac + " "
                numList[indexes[0]] -= 1
                numList[indexes[1]] -= 1
        print finalString[:-1]
        counter += 2
    f.close()

Senator()