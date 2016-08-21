import sys, copy;

def solve():
    #print(k,c,s)
    if k == s:
        return ' '.join(str(x+1)for x in range(k))
    if s * c < k:
        return 'IMPOSSIBLE'
    tile = 1
    res = []
    for i in range(0, s):
        position = 0
        #print('i:', i, ' pos:', position)
        for j in range(0, c):
            #print('j:', j, ' pos:', position)
            position *= k
            position += tile - 1
            tile+=1
            if tile>k:
                tile=1
        #print('i:', i, ' pos:', position)
        res.append(position)
    return ' '.join(str(x+1)for x in res);

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print( inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    #print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        k,c,s = map(int, f.readline().split())
        #print(k,c,s)
        x = solve()
        #print(x)
        file.write(str(x) + "\n")
file.close()            








