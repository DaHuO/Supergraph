import glob
import os.path as path
from shutil import copyfile

def writeLine(case, answer) :
    outF.write('Case #'+str(case+1)+': '+answer)

g = glob.glob('C:\\A\\*.in')
d = dict()
for item in g :
    d[item] = path.getmtime(item)
inF = open(sorted(d, key=d.__getitem__)[-1], 'r')
outF = open(sorted(d, key=d.__getitem__)[-1].replace('.in', '.out'), 'w')
copyfile('thelastword.py', 'C:\\A\\solve.py')

n = int(inF.readline())
case = 0

for line in inF :
    answer = line[0]
    for letter in line[1:] :
        if letter < answer[0] :
            answer += letter
        else :
            answer = letter+answer
    writeLine(case, answer)
    case += 1