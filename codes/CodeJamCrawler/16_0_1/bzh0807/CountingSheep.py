#Bill Zhang
#Counting Sheep
#Google Code Jam

def readFile():
    file = open('A-large.in', 'r')
    fileout = open('sheepout.txt', 'w')
    num = int(file.readline())
    for n in range(num):
        x = int(file.readline())
        if n != num-1:
            fileout.write("Case #"+str(n+1)+": "+str(sleepTime(x))+"\n")
        else:
            fileout.write("Case #"+str(n+1)+": "+str(sleepTime(x)))

def sleepTime(n):
    if n == 0: return 'INSOMNIA'    
    orr = n    
    visited = set([])
    it = 0
    while len(visited) < 10:
        it += 1
        string = str(n)
        for i in string:
            visited.add(i)
        n += orr
    #print(n, n%orr == 0)
    return int(n*(it)/(it+1))

readFile()
#print(sleepTime(166))