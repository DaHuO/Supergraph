import sys, copy;

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
#indicators = ["Z", "O", "W", "T", "V"

def solve(imd,s):
    res = '';
    nc = [0 for x in range(10)]
    while s.count('Z') > 0:
        for v in numbers[0]:
            s = s.replace(v, "", 1)
        nc[0]+=1
    while s.count('W') > 0:
        for v in numbers[2]:
            s = s.replace(v, "", 1)
        nc[2]+=1
    while s.count('U') > 0:
        for v in numbers[4]:
            s = s.replace(v, "", 1)
        nc[4]+=1
    while s.count('X') > 0:
        for v in numbers[6]:
            s = s.replace(v, "", 1)
        nc[6]+=1
    while s.count('G') > 0:
        for v in numbers[8]:
            s = s.replace(v, "", 1)
        nc[8]+=1
    while s.count('T') > 0:
        for v in numbers[3]:
            s = s.replace(v, "", 1)
        nc[3]+=1
    while s.count('F') > 0:
        for v in numbers[5]:
            s = s.replace(v, "", 1)
        nc[5]+=1
    while s.count('O') > 0:
        for v in numbers[1]:
            s = s.replace(v, "", 1)
        nc[1]+=1
    while s.count('S') > 0:
        for v in numbers[7]:
            s = s.replace(v, "", 1)
        nc[7]+=1
    while s.count('N') > 0:
        for v in numbers[9]:
            s = s.replace(v, "", 1)
        nc[9]+=1
    r = '';
    if s != '\n':
        print("Error: s not empty: ", imd, " ", s )
    """for i,n in enumerate(numbers):
        doubleE = (i == 3 or i == 7)
        d9 = i == 9
        while all(x in s for x in n) and (doubleE and s.count('E') >= 2 or not doubleE) and (d9 and s.count('E') >= 2 or not d9):
            if all(x in s for x in n):
                for v in n:
                    s = s.replace(v, "", 1)
                s += str(i)"""
    for i,n in enumerate(nc):
        r += str(i)*n
    return r;

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        s = f.readline()
        file.write(str(solve(i,s)) + "\n")
file.close()            








