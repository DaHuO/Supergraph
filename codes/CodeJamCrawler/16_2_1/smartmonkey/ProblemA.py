

#Read python file

#infl = open('file.in','r+')
#infl = open('A-small-attempt1.in','r+')
infl = open('A-large.in','r+')
#outfl = open('Asmall.out','w')
outfl = open('Alarge.out','w')

cN = int(infl.readline())
#leAr = "ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE"
#letters = list(leAr)
#letters.sort()
#print(letters)
#print(leAr)


for case in range(1,cN+1):
    numE,numF,numG,numH,numI,numN,numO,numR,numS,numT,numU,numV,numW,numX,numZ=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    totaln = [0,0,0,0,0,0,0,0,0,0]
    str1 = infl.readline()
    for i in range(0,len(str1)):
        c = str1[i]
        if (c=='Z') :
            numZ +=1
        elif (c=='X'):
            numX +=1
        elif (c=='W'):
            numW +=1
        elif (c=='V'):
            numV +=1
        elif (c=='U'):
            numU +=1
        elif (c=='T'):
            numT +=1
        elif (c=='S'):
            numS +=1
        elif (c=='R'):
            numR +=1
        elif (c=='O'):
            numO +=1
        elif (c=='N'):
            numN +=1
        elif (c=='I'):
            numI +=1
        elif (c=='H'):
            numH +=1
        elif (c=='G'):
            numG +=1
        elif (c=='F'):
            numF +=1
        elif (c=='E'):
            numE +=1

    # check the result
    # cross zero
    if (numZ!=0):
        totaln[0]=numZ
        numE -= numZ
        numR -= numZ
        numO -= numZ
        numZ = 0

    if (numW!=0):
        totaln[2]=numW
        numT -= numW
        numO -= numW
        numW = 0

    if (numU!=0):
        totaln[4]=numU
        numF -= numU
        numO -= numU
        numR -= numU
        numU = 0

    if (numX!=0):
        totaln[6]=numX
        numS -= numX
        numI -= numX
        numX = 0

    if (numG!=0):
        totaln[8]=numG
        numE -= numG
        numI -= numG
        numH -= numG
        numT -= numG
        numG = 0

    if (numF!=0):
        totaln[5]=numF
        numI -= numF
        numV -= numF
        numE -= numF
        numF = 0

    if (numH!=0):
        totaln[3]=numH
        numT -= numH
        numR -= numH
        numE -= 2* numH
        numH = 0

    if (numS!=0):
        totaln[7]=numS
        numE -= 2*numS
        numV -= numS
        numN -= numS
        numS = 0

    if (numO!=0):
        totaln[1]=numO
        numN -= numO
        numE -= numO
        numO = 0

    if (numE!=0):
        totaln[9]=numE
        print(numE)
        print(numN)
        numE = 0

    tele=''
    for i in range(0,10):
        if totaln[i] != 0 :
            for s in range(0,totaln[i]) :
                tele += str(i)
    result ="Case #{}: {}\n".format(case,tele)
    print (str1)
    print(result)
    outfl.write(result)


infl.close()
outfl.close()
