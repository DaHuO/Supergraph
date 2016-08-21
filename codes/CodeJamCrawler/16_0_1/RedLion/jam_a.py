def checkMissing(b):
    global nums
    global missing
    val = int(b)
    if nums[val] != 1:
        nums[val] = 1
        missing = missing - 1
    #print(nums)
        
def decodeNum(a):
    s = str(a)
    #print(s + "-"+str(len(s)))
    count= 0
    while count < len(s):
        val = s[count]
        #print("Value: " + val)
        checkMissing(val)
        count = count + 1
        
N = 0
i = 1
nums = [0,0,0,0,0,0,0,0,0,0]
missing = 10
       #0,1,2,3,4,5,6,7,8,9

rownum= 0
cases = []
output = []
file = open('A-large.in', 'r')
caseNum = 0
caseVal = 1
for row in file:
    print(row)
    if rownum == 0:
 #       print ("Number of cases: "+ row)
        caseNum = row
        rownum = rownum + 1
    else:
        cases.append(int(row))
 #       print(cases) 
for x in cases:
    N = x
    i = 1
    nums = [0,0,0,0,0,0,0,0,0,0]
    missing = 10
    while i <= N * 100:
        #print(str(i) + ": Iteration")
        n = i * N
        decodeNum(n)
        if(missing == 0):
 #           print("Case #"+str(N)+": " + str(n))
            output.append("Case #"+ str(caseVal)+": " + str(n)+"\n")
            break
        i = i + 1
    if(missing > 0):
       # print("Case #"+str(N)+": INSOMNIA")
        output.append("Case #"+ str(caseVal)+": INSOMNIA\n")
    caseVal = caseVal + 1

file = open("outputlarge1.txt", "w")

for y in output:
    print(str(y))
    file.write(y)

file.close()


    

