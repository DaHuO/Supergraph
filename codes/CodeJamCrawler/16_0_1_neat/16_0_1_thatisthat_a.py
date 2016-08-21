import math

FILE = open("a.in", "r")
OUT = open("o.txt", "w")

def notDone(a):
    for x in a:
        if (x == 0):
            return True
    return False

i = 0
for line in FILE:
    i += 1
    if (i == 1):
        continue
    x = int(line)
    if (x == 0):
        OUT.write("Case #" + str(i - 1) + ": INSOMNIA\n")
        continue

    numbersSeen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lastnumber = 0
    N = 1
    while (notDone(numbersSeen)):
        lastnumber = N * x
        tmp = lastnumber
        while (tmp != 0):
            digit = tmp % 10
            tmp = math.floor(tmp/10)
            numbersSeen[digit] = 1
        N += 1
    OUT.write("Case #" + str(i - 1) + ": " + str(lastnumber) + "\n")

FILE.close()
