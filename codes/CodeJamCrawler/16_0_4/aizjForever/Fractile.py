def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
contentsRead = readFile("D-small-attempt0.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    K = int(c.split(" ")[0])
    contentsToWrite += "Case #%d: " % count
    for i in range(1,K+1):
        contentsToWrite += "%d " % i
    contentsToWrite = contentsToWrite[:-1]
    contentsToWrite += "\n"
    count += 1
writeFile("out.txt",contentsToWrite)