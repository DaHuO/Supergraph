f= open("B-large.in", 'r')
output = open("outputPanL.txt", 'w')
t = f.readline()

#t= raw_input()
t = int(t)
case = 1


   
   
for a0 in xrange(t):
    inp = f.readline()
    pancakeL = [x for x in inp]
    flips = 0
    plusPassed = False
    prevPan = pancakeL[0]
    neg = False
    for x in pancakeL:
        if x == '+':
            plusPassed = True
            if x != prevPan:
                flips += 1
            neg = False
        elif x == '-': 
            if x != prevPan:
                flips += 1
            neg= True
        prevPan = x
    if neg:
        flips += 1
    output.write("Case #" + str(case) + ": " + str(flips) + '\n')
    case += 1
    
f.close()
output.close()