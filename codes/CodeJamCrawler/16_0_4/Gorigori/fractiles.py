if __name__ == '__main__':
    with open("D-small-attempt0.in") as inputFile:
        with open("output.txt", "w") as outputFile:
            inputFile.readline()
            for lineNum,line in enumerate(list(inputFile)):
                k,c,s = line.split()
                solve = " ".join([str(n) for n in range(1,int(k)+1)])
                outputFile.write("Case #{0}: {1}\n".format(lineNum+1, solve))