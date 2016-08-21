#!/usr/bin/python
import math
import sys

f = open("sample.txt")
T = int(f.readline())
(N, J) = f.readline().strip().split()
J=int(J)
N=int(N)
input = "1"
for i in range(0, N-2):
    input += "0" 
input = input+"1"
input = list(input)
print "Case #1:"

def isprime(a, base):
    j=0
    res = 0
    for n in list(a):
        if n == "1":
            res += math.pow(base, j)
        j += 1
    res = int(res)
    return all(res % i for i in xrange(2, int(math.sqrt(res))))

def multiple(a, base):
    j=0
    res = 0
    for n in list(a):
        if n == "1":
            res += math.pow(base, j)
        j += 1
    res = int(res)
    for i in xrange(2, res):
        if res % i == 0:
            return i

def checkinput(input):
    ret = []
    for i in range(2,11):
        if isprime(input, i) :
            return False
        else:
            ret.append(str(multiple(input, i)))
    return ret 


def printoutput(input):
    global validinputs, res_count
    rev_input = list(input)
    rev_input.reverse()
    res = checkinput(''.join(rev_input))
    if res and "".join(input) not in validinputs:
        res_count += 1
        validinputs.append(''.join(input))
        print "%s %s" % ( "".join(input), " ".join(res))
        if res_count == J:
            sys.exit(0) 

validinputs = []
res_count = 0

for i in range(1, N-1):
    input[i] = "1" 
    printoutput(input)
    input[i] = "0"

for i in range(1, N-1):
    for j in range(1, N-1):
        if i != j:
            input[i] = input[j] = "1"
            printoutput(input)
            input[i] = input[j] = "0"

for i in range(1, N-1):
    for j in range(1, N-1):
        for k in range(1, N-1):
            if i != j and j != k:
                input[i] = input[j] = input[k] = "1"
                printoutput(input)
                input[i] = input[j] = input[k] = "0"
