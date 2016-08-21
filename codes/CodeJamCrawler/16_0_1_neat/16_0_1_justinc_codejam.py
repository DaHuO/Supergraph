def find(n,case):
    if n == 0:
        print "Case #"+str(case)+": INSOMNIA"
        return
    found = set()
    lastnumber = 0
    multiplier = 1  
    while len(found) < 10:
        new = multiplier * n
        lastnumber = new
        for digit in str(new):
            found.add(digit)        
        multiplier = multiplier + 1
    print "Case #"+str(case)+": " + str(lastnumber)

f = open('workfile', 'r')
for i,line in enumerate(f):
    if i != 0:
        find(int(line),i)

#for i, x in enumerate([0,1,2,11,37,7,189,137,111,48,124,64,40,197,117,200,135,44,41,59,84,123,115,95,4,19,77,185,122,75,132,10,177,192,53,21,103,9,151,181,157,6,82,105,23,152,180,78,76,20,55,34,93,159,80,47,8,172,131,32,57,176,71,3,136,100,106,174,162,5,125,54,25,173,182,114,148,18,28,92,166,147,141,46,65,120,36,144,175,60,96,87,42,183,171,49,24,79,33,97]):
#    find(x,i+1)

