uniqdigits = "0123456789"

n = int(input())

for i in range(1,n+1):
    k = int(input())
    c = []
    sleep = False
    for j in range(1,100):
        b = k*j

        for digit in str(b):
            c.append(digit)
            digitcount = 0
            for alpha in uniqdigits:
                if alpha in c:
                    digitcount += 1
                if digitcount == 10:
                    print("Case #" + str(i) + ": " + str(b))
                    sleep = True
                    break
            if sleep == True:
                break
        if sleep == True:
            break

    if sleep == False:
        print("Case #" + str(i) + ": INSOMNIA")
