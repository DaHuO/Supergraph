import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.ERROR)


instances = [(32,500)] #[(N,16)]


def as_d_ary(s,d):
    n = 0
    f = 1
    while s > 0:
        n = f* (s%10) + n
        f = d*f
        s = s/10
    return n
        


def set_bit(N,b):
    return N+10**b

def binary_as_base_10(s):
    n = 0
    f = 1
    while s > 0:
        n = f* (s%2) + n
        f = 10*f
        s = s/2
    return n


def check_jamcoin(n):
    j = n
    while j > 0:
        if j%10 > 1:
            print "Bad Jamcoin", n
            exit(0)
            return
        j = j/10
    #print "Good Jamcoin", n

def instance(inst):
    (N,J) = inst
    B = N-1
    half = B/2
    f1 = set_bit(0,B-half)
    f1 = set_bit(f1,0)
    init_mask = set_bit(0,half)
    init_mask = set_bit(init_mask,0)
    lines = []
    if (J >= 2**(half-1)):
        return "ERROR: My algorithm doesn't work."
    for i in xrange(J):
        k = binary_as_base_10(i)
        f2 = init_mask + k*10
        jamcoin = f1*f2
        #print jamcoin, f1,f2
        line = "%d" % jamcoin
        check_jamcoin(jamcoin)
        for i in range(2,11):
            factor = i**(B-half) + 1
            if as_d_ary(jamcoin,i)%factor != 0:
                print "stupid", jamcoin, as_d_ary(jamcoin,i), factor,i
                exit(0)
            line = "%s %d" % (line,factor)
        lines.append(line)
    return lines
            
            
            
def check_output(result):
    for line in result:
        a = line.split()
        n = int(a[0])
        for x in range(1,len(a)):
            if (as_d_ary(n,x+1)%int(a[x]) != 0):
                print "error in output"
                exit(0)
    
out_line_no = 1
for x in instances:
    print "Case #1:"
    result = instance(x)
    check_output(result)
    for x in result:
        print x


