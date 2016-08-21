import math
from collections import Counter

class Importer:
    ''' Reads the file, and queues up inputs'''
    def __init__(self,file):
        self.file = file
        self.fhandle = open(self.file, 'r')
        self.T = int(self.fhandle.readline())

    def pop(self):
        word = list(self.fhandle.readline().strip())
        return word

class Exporter:
    ''' writes output in proper format, line by line'''
    def __init__(self,file):
        self.file = file
        with open(self.file, 'w'): pass
        self.fhandle = open(self.file, 'w')
        self.ind = 1


    def put(self,ans):
        outs = 'Case #'+str(self.ind)+':'
        outs += ' '+str(ans)
        outs+='\n'
        self.fhandle.write(outs)
        self.ind += 1

def removeLetters(count,S):
    stringLetters = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    toKill = []
    for i in range(len(count)):
        toKill.extend(list(stringLetters[i])*count[i])
    c1 = Counter(S)
    c2 = Counter(toKill)
    diff = c1-c2
    return list(diff.elements())

class Runner(object):
    ''' Run algo one case at a time'''

    def run(self, S):
        pcount = [0]*10
        primaries = ['Z', '','W','','U','','X','','G','']
        for i in range(len(S)):
            if S[i] in primaries:
                ind = primaries.index(S[i])
                pcount[ind]+=1
        tempS = removeLetters(pcount,S)
        scount = [0]*10
        seconds = ['', 'O','','H','','F','','S','','']
        for i in range(len(tempS)):
            if tempS[i] in seconds:
                ind = seconds.index(tempS[i])
                scount[ind]+=1

        tempS = removeLetters(scount,tempS)

        scount[9] = len(tempS)/4

        fcount = [pcount[i]+scount[i] for i in range(10)]
        print(fcount)
        fin = [str(i)*int(fcount[i]) for i in range(10)]
        return ''.join(fin)




if __name__=='__main__':
    print(Runner)
    read = Importer('A-large.in')
    sol = Runner()
    write = Exporter('output.txt')
    for i in range(read.T):
        arg = read.pop()
        ans = sol.run(arg)
        print(ans)
        write.put(ans)
