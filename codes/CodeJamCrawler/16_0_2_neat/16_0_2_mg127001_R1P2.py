def output(f, case, *results):
    print("Case #{0:d}: {1:d}".format(case+1, *results), file=f)

def getNextChunkSize(line, l, i):
    #print ("getNextChunkSize: START", line, l, i)
    if not (i < l):
        #print ("getNextChunkSize: END", 0)
        return 0
    size = 1
    while i+size < l and line[i+size] == line[i+size-1]:
        size += 1
    #print ("getNextChunkSize: END", size)
    return size

def findSwaps(line):
    #print ("findSwaps: START", line)
    count = 0
    i = 0
    l = len(line)
    if i < l and line[0] == '-':
        i += getNextChunkSize(line, l, i)
        count += 1
    while i < l:
        sizePositive = getNextChunkSize(line, l, i)
        sizeNegative = getNextChunkSize(line, l, i+sizePositive)
        i += sizePositive + sizeNegative
        if sizeNegative:
            count += 2
    #print ("findSwaps: END", count)
    return count

def main():
    fName = 'R1P2_large0'
    with open(fName + '.txt') as fIn, open(fName + '.out.txt', 'w') as fOut:
        fIn.readline()
        for i, line in enumerate(fIn):
            output( fOut, i, findSwaps(line.strip()) )

if __name__ == '__main__':
    main()
