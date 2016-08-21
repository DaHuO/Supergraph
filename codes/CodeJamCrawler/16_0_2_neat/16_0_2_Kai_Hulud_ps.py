tT = raw_input()
try:
    T = int(tT)
except ValueError:
    print("Cases? %s" % tT)
    T = 0
Symb = {'+','-'}
pnckStk = range(T)
iti = 0
# 0<=T<=100 : Case#s
for Tcase in range(1,T+1):
    allPos = False
    flipsN = 0
    pnckStki = pnckStk[iti] = range(0);
    iti+=1
    try:
        tN = raw_input()
        strgN = str(tN)
    except EOFError or ValueError:
        flipsN=0
        break
    ipcMAX = len(strgN)

    strg = strgN
    itrn = 0
    while(not(allPos)):
        #One Flips Worth of Actions
        posTail = False
        negTail = False
        temPstk = range(0)
        for charS in strgN:
            nomC=str(charS)
            pnckStki.insert(itrn, nomC)
            temPstk.append(nomC)
            if (itrn+1 < ipcMAX):
                if strg[itrn]=='+' and not negTail:
                    if strg[itrn+1]=='+':
                        if itrn+1==ipcMAX:
                            allPos = True
                            posTail = True
                            negTail = False
                            break
                        else:
                            posTail = True
                            negTail = False
                    else:
                        posTail = False
                        negTail = True
                        flipsN+=1
                        for itrsp in range(0,len(temPstk)):
                            pnckStki[itrsp]='-'
                elif strg[itrn]=='-' and not posTail:
                    if strg[itrn+1]=='+':
                        posTail = True
                        negTail = False
                        flipsN+=1
                        for itrsn in range(0,len(temPstk)):
                            pnckStki[itrsn]='+'
                    else:
                        posTail = False
                        negTail = True
            else:
                if len(pnckStki)==1:
                    if str(pnckStki[itrn])=="-":
                        pnckStki="+"
                        flipsN=1
                    else:
                        flipsN=0
                else:
                    if(negTail):
                        flipsN+=1
                        for itrsn in range(0,len(temPstk)):
                            pnckStki[itrsn]="+"
                allPos = True
            itrn+=1
    print("Case #%s: %s" % (Tcase, flipsN))
