f = open("D:/A-small-attempt1.in", "r")
p = open("D:/A-small-attempt1.out", "w")
t = int(f.readline())

for i in xrange(t):
    n = int(f.readline())
    m = 1
    if n == 0:
        p.write("Case #" + str(i+1) + ": INSOMNIA\n")
        continue
    digits = [0] * 10
    while True:
        for j in str(n*m):
            digits[int(j)] = 1
        if digits.count(1) == 10:
            break
        m += 1
    p.write("Case #" + str(i+1) + ": " + str(m*n) + "\n")

f.close()
p.close()