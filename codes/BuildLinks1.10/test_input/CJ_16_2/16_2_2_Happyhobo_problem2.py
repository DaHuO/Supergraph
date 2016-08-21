def read_words(afile):
    words = []
    for line in afile:
        words.append(line.strip())
    return words


filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text


for x in range(int(T)):
    string = aList[x].split(" ")
    C = string[0]
    J = string[1]

    mini = 10000000
    bestF = 10000000
    bestS = 10000000

    herp = len(C)
    derp = len(J)

    for i in range(10**herp):
        for j in range(10**derp):
            isGood = True

            iss = str(i)
            jss= str(j)
            if(len(iss) < herp):
                iss = "0"+iss
            if(len(iss) < herp):
                iss = "0"+iss
            if(len(jss) < derp):
                jss = "0"+jss
            if(len(jss) < derp):
                jss = "0"+jss
            
            
            if((len(iss) == herp) and (len(jss) == derp)):
                for c in range(herp):
                    if(C[c] != "?" and iss[c] != C[c]):
                        isGood = False
                        break
                if(not isGood):
                    break
                for b in range(derp):
                    if(J[b] != "?" and jss[b] != J[b]):
                        isGood = False
                        break

                if(isGood):
                   
                    diff = abs(i - j)
                    if(diff < mini):

                        mini = diff
                        bestF = iss
                        bestS = jss
                    elif(diff == mini && iss < int(bestF)):
                        if(iss < int(bestF):
                            mini = diff
                            bestF = iss
                            bestS = jss
                        if(jss < int(bestS)):
                            mini = diff
                            bestF = iss
                            bestS = jss
    for i in range(len(C)):
        if(C[i] == "?" and J[i] == "?" and str(bestF)[i] == str(bestS)[i]):
            m = list(str(bestF))
            m[i] = "0"
            bestF = ""
            for a in m:
                bestF+=a
            n = list(str(bestS))
            n[i] = "0"
            bestS = ""
            for b in n:
                bestS+=b
            
    
    print "Case #"+(str(x+1))+": "+str(bestF)+" "+str(bestS)
    





