from sys import *

fin = open(argv[1], "r")
fout = open(argv[2],"w")
T = int(fin.readline())
count = 1

for line in fin:
    line = line.strip('\n')
    ans=0
    while line.count('+') != len(line) :
        if line.count('-') == len(line):
            ans += 1
            line = len(line)*'+'
            continue
        for i in range(1,len(line)):
            if line[i]!=line[i-1] :
                line = i*line[i] + line[i:]
                ans += 1
    fout.write('Case #'+str(count)+": "+str(ans)+'\n')
    count += 1
print 'done'
