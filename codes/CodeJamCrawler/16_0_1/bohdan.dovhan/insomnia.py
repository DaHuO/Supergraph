import sys, copy, math;

def solve():
    if n == 0:
        return 'INSOMNIA'
    m = n
    sheepHappy = False
    digits = [False for x in range(10)]
    while not sheepHappy:
        x = m
        #print('m=',m,' x=',x)
        #print('digits=',digits)
        while x > 0:
            #print('x=',x)
            digits[x % 10] = True
            #print('x % 10=',x % 10,'digits=',digits)
            x//=10
            #print('x=',x)
            if all(digits):
                break
        sheepHappy = all(digits)
        #print('digits=',digits)
        #print('sheepHappy=',sheepHappy)
        if sheepHappy:
            rez = m
        m+=n
        #print('digits=',digits)
    return rez

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print( inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        n = int(f.readline())
        x = solve()
        file.write(str(x) + "\n")
file.close()            








