import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

for line in fileinput.input():
    if line_no == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        a = line.split()
        K = int(a[0])
        C = int(a[1])
        S = int(a[2])
        instances.append((K,C,S))
    line_no+=1


def instance(inst):
    (K,C,S) = inst
    if K==S:
        output = ""
        for x in xrange(1,K+1):
            output = "%s%d " % (output, x)
        return output
    else:
        if S*C < K:
            return "IMPOSSIBLE"
        else:
            line = ""
            place = 0
            while place < K:
                current = 0
                for y in xrange(C):
                    current = place*(K**y)
                    place = place + 1
                    if place == K:
                        break

                line = "%s%d " % (line, current+1)
            return line


def check_output(instance,line):
    (K,C,S) = instance
    if line is "IMPOSSIBLE":
        if K <= C*S:
            print "ERrorr"
            exit(0)
        return
    check_these = [int(x) for x in line.split()]
    for x in range(K):
        place = x
        checked = False
        for y in check_these:
            for z in range(C):
                if ((y-1)/(K**z))%K == place:
                    checked = True
        if not checked:
            print place, " is not checked."
            print K,C,S
            print line
            exit(0)

out_line_no = 1
for x in instances:
    result = instance(x)
    check_output(x,result)
    print "Case #%d: %s" % (out_line_no, instance(x))
    out_line_no+=1




