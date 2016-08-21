import sys

FIN = sys.argv[1]
fd = open(FIN, 'r')

ncases = int(fd.readline()[:-1])

for case in range(1, ncases+1):
    DIGITS = [False]*10

    start = int(fd.readline()[:-1])
    if start*2 == start:
        print("Case #" + str(case) + ": INSOMNIA")
        continue

    num = 0
    while False in DIGITS:
        num += start
        for dig in str(num):
            DIGITS[int(dig)] = True
        
    print("Case #" + str(case) + ": " + str(num))

