with open("A-large.in") as f:
    lis=[]
    for line in f:
        line = line.split()
        line=[int(i) for i in line]
        lis.append(line[0])
def maker(N):
    numlist=[]
    i=0
    if (N==0):
        return "INSOMNIA"
    while (len(numlist)<10):
        for x in str(N*(i+1)):
            if (not(int(x) in numlist)):
                numlist.append(int(x))
        i+=1
    return N*(i)
f=open("Submit2.txt","w")
for i in range(lis[0]):
    print >>f, "Case #%s: %s"%(i+1,maker(lis[i+1]))
f.close()


    
    
    

    