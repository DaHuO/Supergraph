def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)


q=open ("output.txt","w")
q.close()
inp = open("B-large.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
for case in range(inpNum):
    n = int(a.pop(0))
    cases = []
    unknown = []
    for i in range((n*2) - 1):
        row = a.pop(0)
        row = row.split(" ")
        cases.append(row)
    bigest = cases[0][n-1]
    for element in cases:
        if int(element[n-1]) > int(bigest):
            bigest = int(element[n-1])
    for i in range(int(bigest)):
        times = 0
        num = i+1
        for q in cases:
            for w in q:
                if int(w)==num:
                    times+=1
        if times%2 == 1:
            unknown.append(num)
    ans = ""
    for i in unknown:
        ans += str(i) + " "
    outp(case,ans)