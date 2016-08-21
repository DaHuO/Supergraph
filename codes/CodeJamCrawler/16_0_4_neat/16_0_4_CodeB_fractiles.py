import fileinput
import sys

i = 0
for line in fileinput.input():
    line = line.strip()
    if i == 0:
        testcases = int(line)
    else:
    	numbers = map(int,line.split())
        k = numbers[0]
        c = numbers[1]
        s = numbers[2]
        sys.stdout.write("Case #%d: " % i)
        j = 1
        while (j<=s):
            sys.stdout.write("%d " % j)
            j += 1
        sys.stdout.write("\n")
    i += 1