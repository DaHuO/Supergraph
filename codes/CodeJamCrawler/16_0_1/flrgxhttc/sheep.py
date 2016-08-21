import numpy as np

def getDigitN(num,place):
    return np.mod(np.divide(num, np.power(10,place)),10)

def searchDigits(seed):
    r = "INSOMNIA"
    if seed ==0 :
        r = "INSOMNIA"
        return r
    digits = {}
    for i in range(10):
        digits[i] = False
    i=0
    while(True):
        num = seed*(i+1)
        nPlaces = np.floor(np.log10(num))
        for j in range(int(nPlaces) +1):
            digits[getDigitN(num,j)] = True
        allDigits = True
        for j in range(10):
            if digits[j] == False:
                allDigits=False
        if allDigits == True:
            r = str(int(num))
            return r
        i+=1

def readInput(name):
    f = open("./result", 'w+')
    x = np.loadtxt(name)
    nExamples = x[0]
    data = x[1:]

    ind = 1
    for d in data:
        ret = searchDigits(int(d))
        line = "Case #"+str(ind)+": "+ret+"\n"
        f.write(line)
        #print line
        ind +=1


        
