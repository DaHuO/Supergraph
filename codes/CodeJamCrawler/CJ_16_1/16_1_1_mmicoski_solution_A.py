# -*- coding: cp1252 -*-
#https://code.google.com/codejam/contest/6254486/dashboard#s=p1
import datetime
import random as r


# =============== debug configs
logDet = False
teste = False


# =============== input file
##nomeIn = "test.txt"
##nomeIn = "A-small-attempt1.in"
nomeIn = "A-large.in"



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
#================================


io = InOut(nomeIn)


T = io.readInt()
print T,"tests"



tini = datetime.datetime.now()
print tini

case=1


##quit()



while True:

    S = io.fin.readline()
    S = S.replace("\n","")

    if logDet: print "K,C,S=",K,C,S

    res = S[0]
    for ch in S[1:]:
        if logDet: print res, ch,
        if ch >= res[0]:
            res = ch + res
        else:
            res = res + ch
        if logDet: print res


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
