def sleep(d):
    for i in range(10):
        if i not in d:
            return False
    return True

def sleepNumber(n):
    if n == 0:
        return "INSOMNIA"

    seenSoFar = {}
    i = 0

    while not sleep(seenSoFar):
        i += 1
        num = i * n
        while num != 0:
            t = num % 10
            seenSoFar[t] = True
            num /= 10

    return i*n

file = "large"
fin = open(file + ".in", 'r')
fout = open(file + ".out", 'w')

cases = int(fin.readline())

for i in range(cases):
    inp = int(fin.readline())
    result = sleepNumber(inp)
    fout.write("Case #" + str(i+1) + ": " + str(result) + "\n")