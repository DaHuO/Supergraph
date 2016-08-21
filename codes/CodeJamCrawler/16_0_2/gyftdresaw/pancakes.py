
'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())

def count_switches(S):
    total = 0
    curr = S[0]
    for c in S:
        if curr != c:
            total += 1
        curr = c
    return total

for i in xrange(trials):

    S = str.strip(infile.readline())
    S += '+'

    result = count_switches(S)
    
    s = "Case #%d: %s\n" % (i+1,result)
    outfile.write(s)
    print s
    
infile.close()
outfile.close()
