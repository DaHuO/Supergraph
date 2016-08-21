def helper(N,count,a):
    num = N*count;
    while (num>0):
        b = num % 10
        if b not in a:
            a.add(b)
        num //= 10
    return;
def count_sheep(N):
    if N == 0 :
        return "INSOMNIA"
    a = set();
    count = 1
    while (len(a) < 10):
        helper(N,count,a)
        count+=1
    return (count-1)*N

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsRead = readFile("A-large.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    N = int(c)
    res = count_sheep(N)
    if type(res) == type("f"):
        contentsToWrite += "Case #%d: INSOMNIA" % count
        contentsToWrite += "\n"
    else:
        contentsToWrite += "Case #%d: " % count
        contentsToWrite += "%d" % res 
        contentsToWrite += "\n"
    count+=1
writeFile("out.txt",contentsToWrite)


