from sys import *

fin = open(argv[1], "r")
fout =  open(argv[2],"w")
T = int(fin.readline())
count = 1
for line in fin:
    number = set(['1','2','3','4','5','6','7','8','9','0'])
    n = line
    a, i, = n, 0
    if int(n) == 0:
        fout.write('Case #' + str(count) + ": " +'INSOMNIA' + '\n')
        count +=1
        continue
    while number:
        i += 1
        a = str(int(n) * i)
        number = number - set(a)
    fout.write('Case #'+str(count)+": "+str(a)+'\n')
    count += 1

