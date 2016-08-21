def getAnswer(pc):
    total = 0
    if pc == "+"*len(pc):
        return 0
    elif pc == "-"*len(pc):
        return 1
    else:
        cur = pc[0]
        for j in range(1,len(pc)):
            if cur == pc[j]:
                continue
            else:
                total = total + 1
                cur = pc[j]
        if pc[-1] == "-":
            total = total +1
        
        return total


fi = open("input.txt","r")
fo = open("output", "w")

t = int(fi.readline().strip())


for i in range(t):
    pc = fi.readline().strip()
    fo.write("Case #{0}: {1}\n".format(i+1,getAnswer(pc)))
    
          
fi.close()
fo.close()