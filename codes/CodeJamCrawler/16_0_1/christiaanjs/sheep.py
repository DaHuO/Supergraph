def allTrue(array):
    for b in array:
        if not b:
            return False
    return True

def getDigits(x, existingDigits):
    y = x
    while y >= 1:
        existingDigits[y % 10] = True
        y = int(y/10)
    return existingDigits

f = open("in.txt", "r")
t = int(f.readline())

g = open("out.txt", "w")

for c in range(t):
    g.write("Case #" + str(c+1) + ": ")
    n = int(f.readline())
    if n == 0:
        g.write("INSOMNIA")
    else:
        digits = [False]*10
        i = 1
        while not allTrue(digits):
            digits = getDigits(n*i, digits)
            i += 1
        g.write(str((i-1)*n))
    if c < t-1:
        g.write("\n")   

f.close()
g.close()
