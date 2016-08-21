import math


class Importer:
    ''' Reads the file, and queues up inputs'''
    def __init__(self,file):
        self.file = file
        self.fhandle = open(self.file, 'r')
        self.T = int(self.fhandle.readline())

    def pop(self):
        N = int(self.fhandle.readline().strip())
        sets = [];
        for i in range(2*N-1):
            nums = self.fhandle.readline().strip().split()
            temp = []
            for x in nums:
                temp.append(int(x))
            sets.append(temp)
        return (N, sets)

class Exporter:
    ''' writes output in proper format, line by line'''
    def __init__(self,file):
        self.file = file
        with open(self.file, 'w'): pass
        self.fhandle = open(self.file, 'w')
        self.ind = 1


    def put(self,ans):
        outs = 'Case #'+str(self.ind)+':'
        for u in ans:
            outs += ' '+str(u)
        outs+='\n'
        self.fhandle.write(outs)
        self.ind += 1


class Runner(object):
    ''' Run algo one case at a time'''

    def run(self, N,sets):



        currList = []
        for i in range(N):

            for s in sets:
                currList.append(s[i])
        missing = []
        counts = list(map(lambda x: currList.count(x),set(currList)))
        missings = list(map(lambda x: x%2,counts))
        vals = list(set(currList))
        for x in range(len(vals)):
            if missings[x] == 1:
                missing.append(vals[x])
        return sorted(missing)


if __name__=='__main__':
    print(Runner)
    read = Importer('B-large.in')
    sol = Runner()
    write = Exporter('output.txt')
    for i in range(read.T):
        (N,sets) = read.pop()
        ans = sol.run(N,sets)
        write.put(ans)
