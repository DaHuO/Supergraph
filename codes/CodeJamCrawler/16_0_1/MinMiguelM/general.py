
filenameInput = "A-large.in"
filenameOutput = "A-large.out"

def countSheep(N):
    numbers = []
    if N==0:
        return "INSOMNIA"
    else:
        i,k=1,0
        while len(numbers) != 10:
            k = N*i
            S = list(str(k))
            for j in S:
                if numbers.count(int(j)) == 0:
                    numbers.append(int(j))
                if len(numbers) == 10:
                    break
            i+=1
    return k

def loadFile():
    f = open(filenameInput,"r")
    tc = int(f.readline())
    s=""
    i=1
    while(i<=tc):
        N = int(f.readline())
        c = countSheep(N)
        s += "Case #"+str(i)+": "+str(c)+"\n" if i<tc else "Case #"+str(i)+": "+str(c)
        i+=1
    saveFile(s)
    f.close()

def saveFile(string):
    f = open(filenameOutput,"w")
    #f.write("Case #",x,": ",y, )
    f.write(string)
    f.close()

loadFile()
