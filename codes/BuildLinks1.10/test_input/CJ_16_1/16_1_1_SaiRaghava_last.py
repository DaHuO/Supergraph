from sys import *

fin = open(argv[1], "r")
fout =  open(argv[2],"w")
T = int(fin.readline())
count = 1
for line in fin:
    for i in xrange (1,len(line)):
        if line[i]>=line[0]:
            line=line[i]+line[0:i]+line[i+1:]
    fout.write('Case #'+str(count)+": "+str(line))
    count += 1
print "done"
