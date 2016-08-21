import glob
import os.path as path
from shutil import copyfile


def writeline(case, answer):
    outF.write('Case #'+str(case+1)+':'+answer+'\n')


g = glob.glob('C:\\A\\*.in')
d = dict()
for item in g:
    d[item] = path.getmtime(item)
inF = open(sorted(d, key=d.__getitem__)[-1], 'r')
outF = open(sorted(d, key=d.__getitem__)[-1].replace('.in', '.out'), 'w')
copyfile('SenateEvacuation.py', 'C:\\A\\solve.py')

n = int(inF.readline())
case = 0
a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(n):
    answer = ""
    c = int(inF.readline())
    m = [[int(y), a[x]] for x, y in enumerate((inF.readline()).split())]
    m = sorted(m)
    while m[c-1][0] > 0:
        answer += ' '
        for j in range(1, c)[::-1]:
            if m[j][0] > m[j-1][0]:
                answer += m[j][1]
                m[j][0] -= 1
                if j < c-1 and (j != c-3 or m[j][0] != 0):
                    answer += m[j+1][1]
                    m[j+1][0] -= 1
                break
        else:
            answer += m[0][1]
            m[0][0] -= 1
            if c != 3 or m[0][0] != 0:
                answer += m[1][1]
                m[1][0] -= 1
    writeline(case, answer)
    case += 1