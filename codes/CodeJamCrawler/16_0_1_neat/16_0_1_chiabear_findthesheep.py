
inputfile = open("sheepbig.txt")

lines = []

for line in inputfile:
    lines.append(line)

inputfile.close()


    
def findTheSheep(startNumber):
    '''
    returns the number when all of the digits have been counted for
    '''
    digits = {}

    for i in range(10):
        digits[str(i)]=False
    
    mult = 1    
    
    if startNumber == 0:
        return "INSOMNIA"
    else:
        while False in digits.values():
            sheep = startNumber * mult
            for d in str(sheep):
                digits[d]=True
            mult+=1
        return sheep
            
newfile = open("outputsheepbig.txt",'w')       

for j in range(1, len(lines)):
    newfile.write("Case #" + str(j) +": " + str(findTheSheep(int(lines[j]))) + '\n')
    #print findTheSheep(int(lines[j]))
    
newfile.close()        
    