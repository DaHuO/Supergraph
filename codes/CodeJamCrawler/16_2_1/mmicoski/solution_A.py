# -*- coding: cp1252 -*-
#https://code.google.com/codejam/contest/6254486/dashboard#s=p1
import datetime
import random as r


# =============== debug configs
logDet = False
teste = False


# =============== input file
##nomeIn = "teste.txt"
nomeIn = "A-small-attempt3.in"
##nomeIn = "D-large.in"



# =============== auxiliary functions
class InOut:
    def __init__(self, nomeIn):
        nomeOut = nomeIn.split(".")[0]+".out"
        self.fin = open(nomeIn,"r")
        self.fout = open(nomeOut,"w")

    # reads one integer
    def readInt(self):
        return int(self.fin.readline())    

    # reads list of integers
    def readIntList(self):
        MN = self.fin.readline().split()
        MN = [int(x) for x in MN]

        return MN

    # reads file in lines
    def readLines(self, qt):
        lines = []
        for i in range(qt):
            line = self.fin.readline()
            lines.append(line)

        return lines

    def writeLine(self, line):
        self.fout.write(line+"\n")

    def endAccess(self):
        self.fin.close()
        self.fout.close()

# =============== functions specific to problem

numb = [
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"]

n2 = [[i,numb[i],len(numb[i])] for i in range(len(numb))]
numb2 = sorted(n2, key=lambda x :x[2], reverse = True)

def buscaDigito(S, dig):
    s2 = S
    achou = True
    for ch in dig:
        if ch in s2:
            ind = s2.index(ch)
            #print s2,ind,ch,
            s2 = s2[0:ind]+s2[ind+1:]
            #print s2
        else:
            achou=False

    if not achou:
        s2 = S
    return s2, achou


result = None

def buscaDigitos(S, digs):
    global result
    opcoes = []
    s2 = S
    for dig in numb2:
        s3,achou = buscaDigito(s2,dig[1])
        #print dig, s3, achou
        if achou:
            digs2 = list(digs)
            digs2.append(dig)

            if s3 == "":
                result = list(digs2)
                #print "achou",digs2
            else:
                s4 = buscaDigitos(s3,digs2)

    digs.append(opcoes)
    return digs
        


    s2 = S
    achou = True
    for ch in dig:
        if ch in s2:
            ind = s2.index(ch)
            #print s2,ind,ch,
            s2 = s2[0:ind]+s2[ind+1:]
            #print s2
        else:
            achou=False

    if not achou:
        s2 = S
    return s2, achou

#================================


io = InOut(nomeIn)


T = io.readInt()
print T,"tests"



tini = datetime.datetime.now()
print tini

case=1


##quit()



while True:

    S = io.fin.readline().replace("\r","").replace("\n","")
    print S

    s = S
    opcoes = []
    digs = []
    if 0:
        for idig in range(len(numb2)):
            dig = numb2[idig][1]
            achou=True
            while achou:
                s, achou = buscaDigito(s, dig)
                #print s, achou, idig
                if achou:
                    digs.append(numb2[idig][0])

    result = None
    buscaDigitos(S, [])
    print "result", result

    rest="OK"
    if result == None: rest = "ERRO"
    print digs, s, rest
    
    
    digs = [x[0] for x in result]

    res = ""
    for ch in sorted(digs):
        res += str(ch)


    # write answer
    log = "Case #%d: %s"%(case, res)

    io.writeLine(log)

    print log

    case += 1

    #did I see all test cases?
    if case > T:
        print "encerrando"
        break

  

    if teste:
        break


#close files
io.endAccess()


tfim = datetime.datetime.now()
print "TEMPO GASTO"
print tini
print tfim
print tfim-tini
