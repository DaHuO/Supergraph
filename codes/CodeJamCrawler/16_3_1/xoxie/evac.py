import sys

f = open(sys.argv[1])
f.readline()

#chr(65) is A

casenum = 1
n = f.readline()
while n != "":
    p = [int(x) for x in f.readline().split()]
    p = zip(p,[chr(x) for x in range(65,65+len(p))])

    output = []
    while len(p):
        #print p, sum([x[0] for x in p])
        p.sort(reverse=True)
        n1,party1 = p[0]
        n2,party2 = p[1]
        left = sum([x[0] for x in p[2:]])
        if left:
            #remove 1
            left = left+(n1-1)+n2
            if left % 2:
                maj = left / 2 + 1
            else:
                maj = left / 2
            if n1 == 1:
                output.append(party1)
                p = p[1:]
            elif (n1-1) >= maj or n2 >= maj:
                #remove 2
                output.append(party1+party2)
                p[0] = (n1-1,party1)
                p[1] = (n2-1,party2)
            else:
                output.append(party1)
                p[0] = (n1-1,party1)
        else:
            output.append(party1+party2)
            if n1-1:
                p[0] = (n1-1,party1)
                p[1] = (n2-1,party2)
            else:
                p = []
        
    output = " ".join(output)
    
    print "Case #{}: {}".format(casenum,output)
    n = f.readline()
    casenum += 1
f.close()
