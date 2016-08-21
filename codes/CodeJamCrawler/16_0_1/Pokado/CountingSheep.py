numberOfNumbers = input()

listOfsheep = []

for i in range(numberOfNumbers):
    listOfsheep.append(input())
    
def countingSheep(staringSheep):
    #print 'Started running function'
    allNumbersList = [0,1,2,3,4,5,6,7,8,9]
    sheepNumbersList = []
    strSheep = str(staringSheep)
    numberSheep = staringSheep
    newNuberofSheep = numberSheep
    i = 1
    if staringSheep != 0:
        while sheepNumbersList != allNumbersList:
            #print sheepNumbersList
            newNuberofSheep = numberSheep * i
            strSheep = list(str(newNuberofSheep))
            for values in strSheep:
                values = int(values)
                if values not in sheepNumbersList:
                    sheepNumbersList.append(values)
            sheepNumbersList.sort()
            i += 1
        return newNuberofSheep
    else:
        return "INSOMNIA"

for i in range(numberOfNumbers):
    sheep = listOfsheep[i]
    answer = str(countingSheep(sheep))
    print "Case #%s: %s" % (i+1, answer)
        
    