for test in range(int(input())):
    n = int(input())
    if n == 0:
        print("Case #" + str(test + 1) + ": INSOMNIA")
    else:
        digitsNotFound = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        i = 0
        while len(digitsNotFound) != 0:
            i+=1
            digitsNotFound = digitsNotFound.difference(set(list(str(i*n))))
            #print("Tried: " + str(i*n) + ", Set: " + str(digitsNotFound))
        print("Case #" + str(test + 1) + ": " + str(i*n))
