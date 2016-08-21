import math

LENGTH = 32
COUNT = 500

def getFactor(n):
    i = 2
    while i <= 100: # We don't need all the jamcoins
        if (n % i == 0):
            return i
        i += 1
    return -1

outputFile = open("problem_c.out", "w")
outputFile.write("Case #1:\n")
c = 0
        
i = 0
while i < 2**(LENGTH-2) and c < COUNT:
    digits = bin(i)[2:]
    digits = '0' * (LENGTH-2-len(digits)) + digits
    digits = '1' + digits + '1'
    jamcoin = digits
    for n in range(2,11):
        f = getFactor(int(digits,n))
        if f == -1:
            jamcoin = ""
            break
        jamcoin += " " + str(f)
    if jamcoin != "":
        outputFile.write(jamcoin + '\n')
        c += 1
        print c
    i += 1

outputFile.close()
