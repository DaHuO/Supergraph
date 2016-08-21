#!/usr/bin/python

def getCount(k, c, s):
    toret = ""
    for ix in range(k):
        toret += str(ix+1) +" "
    return toret
    t = k-c + 1
    if t< 0:
        t=1
    if s < t:
        return "-1"
    else:
        toret = ""
        if c == 1:
            for ix in range(k):
                toret += str(ix+1) +" "
        else:
            ne = 1
            pow = 1
            for ix in range(c-1):
                pow = pow * k
            for ix in range(c-1):
                ne += pow
                pow = pow/k

            if t == 1:
                return str(ne)
            ste = k-t+2
            while ste <= k:
                toret += str(ste) + " "
                ste += 1
            toret += str(ne)
        return toret

f = open('A.small.txt', 'r')
tc = int(f.readline())
#print tc
for index in range(tc):
    nums = f.readline().rstrip().split(" ")
    k = int(nums[0])
    c = int(nums[1])
    s = int(nums[2])
    #print k ,c, s

    ct = getCount(k,c,s)
    if ct == "-1":
        print "CASE #" + str(index+1) + ": IMPOSSIBLE"
    else:
        print "CASE #" + str(index+1) + ": " +  str(ct)

'''
for line in f:
        print line
'''
