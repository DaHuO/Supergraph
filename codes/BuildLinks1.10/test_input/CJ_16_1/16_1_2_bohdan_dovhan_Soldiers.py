import sys;

def tp(a,m,n):
    return [[a[i][j] for i in range(0,n)] for j in range(0,m)]
def md(a,n):
    return [a[i][i] for i in range(0,n)]
def ad(a,n):
    return [a[i][n-1-i] for i in range(0,n)]

def solve():
    b = [False for i in range(0,2500)]
    for j in range(0,2*n-1):
        for k in range(0,n):
            b[a[j][k]-1] = not b[a[j][k]-1]
    x = []
    for j in range(0,2500):
        #print(j)
        if b[j]:
            x.append(j+1)
    x.sort()
    return ' '.join(map(str,x));

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
#print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    #print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        n = int(f.readline())
        #print( "n",n)
        a = [list(map(int, f.readline().split())) for j in range(0,2*n-1)]
        """for j in range(0,2*n-1):
            print(' '.join(map(str,a[j])))"""
        file.write(str(solve()) + "\n")
file.close()            








