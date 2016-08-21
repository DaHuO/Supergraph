def flipStack(a):
    global stacks
    global ordered
    global flips 
    #print("location: " + str(a))
    c = 0
    flips = flips + 1
    while c <= a:
        if(stacks[c] == 1):
            stacks[c] = 0
        else:
            stacks[c] = 1
        c = c + 1

    bb = 0
    while bb < len(stacks):
        if(stacks[bb] == 1):
            ordered = 1111
        else:
            ordered = -1
            break
        bb = bb + 1
 #   print("ordered?:" + str(ordered))
 #    print(stacks)
    

pancakes= ""
stacks = []
rownum= 0
cases = []
output = []
ordered = -1
file = open('B-large.in', 'r')
caseNum = 0
caseVal = 1
flips = 0
for row in file:
    print(row)
    if rownum == 0:
        print ("Number of cases: "+ row)
        caseNum = row
        rownum = rownum + 1
    else:
        cases.append(row.strip( '\n' ))
print(cases) 
for x in cases:
    pancakes = x
#    print(x)
    stacks = []
    flips = 0
    z = 0
    while z < len(x):
        if(x[z] == "+"):
            stacks.append(1)
        else:
            stacks.append(0)
        z = z + 1
        
    i = len(x)-1
    j = 0
    bb = 0
    while bb < len(stacks):
        if(stacks[bb] == 1):
            ordered = 1111
        else:
            ordered = -1
            break
        bb = bb + 1
 #   print(stacks)
    while j < (len(x)* 2): 
        while i >= 0:
            #print(str(i) + ": Iteration")
            if(stacks[i] == 0):
                flipStack(i)
            if(ordered == 1111):
                output.append("Case #" +str(caseVal)+": "+ str(flips)+"\n")
                caseVal = caseVal + 1
                break
            i = i - 1
        if(ordered == 1111):
                break
 
        i = 0
        j = j + 1

file = open("outputlargeb11111111.txt", "w")

for y in output:
    print(str(y))
    file.write(y)

file.close()


    

