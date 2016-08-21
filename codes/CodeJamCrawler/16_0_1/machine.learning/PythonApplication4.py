data = open("A-small-attempt0.in")
boolVector = [False] * 10
numCase = int(data.readline())
def VectorCheck(boolVector):
    for i in boolVector:
        if i == False:
            return False
            break
    return True    

for i in range(numCase):
    boolVector = [False]*10
    line = data.readline()
    print line
    line = int(line)
    copy_line = line
    line = str(line)
    if line == "0":
        print "INSOMNIA"
        result = "INSOMNIA"
        otvety = open("output.txt", "a")
        otvety.writelines("Case #%d: %s \n" % (i+1, result))
        otvety.close()
    else:
        while (VectorCheck(boolVector) == False):
            for l in range(len(line)):
                boolVector[int(line[l])] = True
                
            
            line = int(line) + copy_line
            line = str(line)
            
        result = int(line) - copy_line
        otvety = open("output.txt", "a")
        otvety.writelines("Case #%d: %d \n" % (i+1, result))
        otvety.close()
    
        


        





#numCace = int(data.readline())
#listOfCaces = data.readlines()
#print listOfCaces
#for i in range(len(listOfCaces)):
#    listOfCaces[i] = int(listOfCaces[i])
#print listOfCaces

#for e in listOfCaces:
#    for n in range(len(e)):
        


    





