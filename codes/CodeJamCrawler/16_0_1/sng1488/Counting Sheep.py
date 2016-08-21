t = int(input())
for i in range(1,t+1):
    n = int(input())
    digitsSeen = [ ]
    tries = 0
    lastNumber = 0
    while(not (len(digitsSeen) == 10) and tries <= 1000):
        tries = tries+1
        lastNumber = tries*n
        for d in range(len(str(lastNumber))):
            if int(str(lastNumber)[d]) not in digitsSeen:
                digitsSeen.append(int(str(lastNumber)[d]))
    if len(digitsSeen)==10:
        print("Case #",i,": ",lastNumber, sep='')
    else:
        print("Case #",i,": INSOMNIA", sep='')
