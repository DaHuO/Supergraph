import sys
fout = open('output.txt', 'w')
sys.stdout = fout

fin = open('A-large.in', 'r')

numCases = int(fin.readline())
for kk in range(0,numCases):
    print("Case #%d: " %(kk+1), end="")
    N = int(fin.readline())
    if N == 0:
        print("INSOMNIA\n", end="")
    else:
        numlist = set()
        currentN = N
        while True:
            newset = set(str(currentN))
            numlist = numlist | newset
            if len(numlist)>9:
                print("%d\n" %currentN, end="")
                break
            else:
                currentN = currentN + N
fin.close()
