import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.ERROR)


nTest = 0
line_no = 0
instances = []

for line in fileinput.input():
    if line_no == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        S = line.rstrip("\n\r")
        instances.append(S)
        logging.debug ("Instance: %s" % S)
    line_no+=1

def instance(inst):
    flips = 0
    for i in range(0,len(inst)-1):
        if inst[i]  != inst[i+1]:
            flips +=1
    if inst[len(inst)-1] == '-':
        flips +=1
    return flips
            
out_line_no = 1
for x in instances:
    result = instance(x)
    if isinstance(result,str):
        print "Case #%d: %s" % (out_line_no, instance(x))
    else:
        print "Case #%d: %d" % (out_line_no, instance(x))
    out_line_no+=1


