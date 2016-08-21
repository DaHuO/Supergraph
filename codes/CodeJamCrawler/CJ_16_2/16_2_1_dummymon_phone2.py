def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)

q=open ("output.txt","w")
q.close()
inp = open("A-large.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
nums = {"Z":"0", "W":"2","U":"4","X":"6","G":"8",}
for ii in range(inpNum):
    n = a[ii]
    n = list(n)
    others = {"H": 0 , "O" : 0 , "S": 0 , "F": 0 , "I": 0}
    total= {"0":0, "1": 0, "2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,}
    for i in n:
        if i in nums:
            total[nums[i]] += 1
        if i in others:
            others[i] += 1
    total["3"] += others["H"] - total["8"]

    total["1"] += others["O"] - total["0"] - total["2"] - total["4"]

    total["7"] += others["S"] - total["6"]

    total["5"] += others["F"] - total["4"]

    total["9"] += others["I"] - total["8"] - total["6"] - total["5"]
    answer = []
    for key in total:
        for i in range(total[key]):
            answer.append(key)
    ans = ""
    answer.sort()
    for i in answer:
        ans += i
    outp( ii ,ans)
