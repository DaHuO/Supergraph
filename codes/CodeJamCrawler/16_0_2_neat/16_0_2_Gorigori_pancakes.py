def sort(s):
    n = len(s)
    flips = 0
    if n==1:
        if s=="-":
            return 1
        else:
            return 0
    else:
        for i in range(1,n):
            if s[i-1]!=s[i]:
                flips+=1
    if s[-1]=="-":
        flips+=1
    return flips

if __name__ == '__main__':
    with open("B-large.in") as inputFile:
        with open("output.txt", "w") as outputFile:
            inputFile.readline()
            for lineNum,line in enumerate(list(inputFile)):
                outputFile.write("Case #{0}: {1}\n".format(lineNum+1, sort(line.split()[0])))