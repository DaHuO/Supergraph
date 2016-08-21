## -*- coding: windows-1251 -*-
"""
5
2 3 2
1 1 1
2 1 1
2 1 2
3 2 3

Case #1: 2
Case #2: 1
Case #3: IMPOSSIBLE
Case #4: 1 2
Case #5: 2 6

Case #1: 3
Case #2: 1
Case #3:IMPOSSIBLE
Case #4: 1 2
Case #5: 2 7
"""

import sys
if len(sys.argv) > 1: filename = sys.argv[1]
else: filename = "in.txt"

inFile = open(filename, "r")
outFile = open("out.txt", "w")

class fractal:
    def resolve(self):
        #print(self.length, self.complexity, self.students)
        if self.length > self.complexity*self.students:
            self.res = "IMPOSSIBLE"
        else:
            self.res = []
            pos = 1
            while pos<=self.length:
                next_pos = min(pos+self.complexity, self.length+1)
                pack = [i for i in range(pos, next_pos)]
                ind = 1
                #print(pack)
                for i in range(len(pack)):
                    ind += (pack[i]-1)*self.length**(self.complexity-i-1)
                self.res.append(ind)
                pos = next_pos

    def __init__(self, case_num, length, complexity, students):
        self.case_num = case_num
        self.length = length
        self.complexity = complexity
        self.students = students
        self.resolve()

    def __repr__(self):
        res = ""
        for i in self.res:
            res += " "+str(i)
        if self.res == "IMPOSSIBLE": res = "IMPOSSIBLE"
        return "Case #{0}:{1}".format(self.case_num, res)

try:
    st = inFile.readline()
    print("file inputs: "+st)
    for i in range(int(st)):
        st = inFile.readline().split()
        length = int(st[0])
        complexity = int(st[1])
        students = int(st[2])
        f = fractal(i+1, length, complexity, students)
        outFile.write("{0}\n".format(f))

finally:
  inFile.close()
  outFile.close()