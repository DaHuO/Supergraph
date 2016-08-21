
'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())


def count_digits(N):
    seen = [False] * 10
    curr = N
    while (sum(seen) != 10):
        digits = [int(x) for x in str(curr)]
        for d in digits:
            seen[d] = True
        curr += N

    return curr-N

for i in xrange(trials):

    N = abs(int(infile.readline()))

    if (N == 0):
        result = "INSOMNIA"
    else:
        result = count_digits(N)
    
    print(N)
    
    s = "Case #%d: %s\n" % (i+1,result)
    outfile.write(s)
    print s
    
infile.close()
outfile.close()
