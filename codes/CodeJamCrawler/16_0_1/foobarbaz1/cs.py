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
        S = int(line)
        instances.append(S)
        logging.debug ("Instance: %d" % S)
    line_no+=1

def number_digits(n,digits):
    while n > 0:
        digits[n%10] = True
        n = n/10

def instance(inst):
    if inst==0:
        return "INSOMNIA"
    else:
        digits = {}
        number_digits(inst,digits)
        n = inst
        i = 1
        while len(digits) < 10:
            i = i+1
            n = inst+n
            number_digits(n,digits)
            logging.debug("Digits")
            logging.debug(digits)
        return n
            
out_line_no = 1
for x in instances:
    result = instance(x)
    if isinstance(result,str):
        print "Case #%d: %s" % (out_line_no, instance(x))
    else:
        print "Case #%d: %d" % (out_line_no, instance(x))
    out_line_no+=1


