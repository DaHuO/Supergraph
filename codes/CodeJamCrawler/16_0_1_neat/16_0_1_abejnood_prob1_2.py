import csv, sys, random, math


#def readFunction():
#sols
x = [0] * 1000002

def solve(n):
    vals = [1 for i in xrange(10)]
    output = n
    count = 0

    while (sum(vals) != 0):
        count += 1
        output = n * count
        outputStr = str(output)
        for i in xrange( len(outputStr) ):
            index = int(outputStr[i])
            if vals[index] != 0:
                vals[index] = 0
    return (count * n)    

for i in xrange(1000000):
    x[i + 1] = solve(i + 1)
    case_num = str(i + 1)
    print "Case #", case_num, ": ",  str(x[i + 1])


target = open("prob1_output_large.txt", 'w')
with open('large.txt','r') as f:
    T = int(f.readline())
    for i in xrange(T):
        val = int(f.readline())
        case_num = str(i+1)
        if val == 0:
            sol_str = 'Case #' + case_num +  ': ' + "INSOMNIA" + '\n'
        else:
            sol_str = 'Case #' + case_num +  ': ' + str(x[val]) + '\n'
        target.write( str(sol_str) )
        
    






