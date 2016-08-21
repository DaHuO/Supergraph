readFile = open("A-large.in")
testCases = eval(readFile.readline())
ans = {}
for t in range(0,testCases):
    temp = [] 	
    N = readFile.readline()
    j = 1
    a = N
    if int(N) == 0:
       ans[t] = "INSOMNIA"
       continue
    while len(temp) < 10:
       a = str(j*int(N))
       j += 1
       for i in range(0,len(a)):
          if a[i] not in temp:
             temp.append(a[i])
    ans[t] = a

outputFile = open("Counting_Sheeps_output.txt",'w')

for i in range(0,len(ans)):

    outputFile.write("Case #%d: %s\n" % (i+1,ans[i]))

