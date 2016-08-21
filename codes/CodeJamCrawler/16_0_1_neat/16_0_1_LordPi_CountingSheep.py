def splitDigits(n):
    l = [];
    for c in list(str(n)):
        l.append(int(c));
    return l;
    
def countSheep(n):
    n0 = n;
    l = [0] * 10;
    while(True):
        dList = splitDigits(n);
        for d in dList:
            l[d] += 1;
        b = True;
        for d in l:
            b = b and (d != 0);
        if(b):
            return n;
        n += n0;

with open("sheepOut.txt","wb") as outFile:
    with open("sheep.txt","rb") as inFile:
        numCases = int(inFile.readline());
        i = 1;
        for line in inFile:
            outFile.write("Case #%d: "%(i));
            i+=1;
            n = int(line);
            if(n==0):
                outFile.write("INSOMNIA\n");
            else:
                outFile.write("%d\n"%(countSheep(n)));

