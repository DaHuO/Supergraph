import fileinput
import logging
import sys
import numpy as np
import string

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

lines = []

for line in fileinput.input():
    lines.append(line)

i=0
while i < len(lines)-1:
    if line_no == 0:
        line = lines[0]
        nTest = int(line)
        logging.debug("%d" % nTest)
        line_no+=1
        i +=1
    else:
        N = int(lines[i])
        line = lines[i+1]
        instances.append((N,line))
        logging.debug ("Instance: %s" % N)
        i += 2


chars = list(string.ascii_uppercase)

def to_chars(runs):
    result = ""
    for x in runs:
        result += chars[x]
    return result

def two_arg_max(cnts):
    m = max(cnts)
    result = []
    cnt = 0
    for i in range(len(cnts)):
        if cnts[i] == m:
            result.append(i)
            cnt+=1
        if (cnt >= 2):
            return result
    return result

def instance(inst):
    (N,row) = inst
    counts = []
    result = ""
    logging.debug("Row %s" % row)
    for x in row.split():
        counts.append(int(x))
    logging.debug("Counts")
    logging.debug(counts)
    total = sum(counts)
    while total >= 0:
        assert(max(counts) > 0)
        runs = two_arg_max(counts) 
        logging.debug ("Len: %d" % len(runs))
        for x in runs:
            logging.debug ("senator running: %d" % x)
        if total%2 == 1:
            runs = runs[:1]
        total -= len(runs)
        for x in runs:
            counts[x] -= 1
        if total > 0:
            result = result + to_chars(runs) + " "
        else:
            result = result + to_chars(runs) 
        logging.debug("Counts")
        logging.debug(counts)
        if (max(counts) > sum(counts)/2):
            print counts
            print max(counts),sum(counts)/2
            assert(False)
        if total == 0:
            break
    return result

out_line_no = 1
for x in instances:
    result = instance(x)
    print "Case #%d: %s" % (out_line_no, result)
    out_line_no+=1


