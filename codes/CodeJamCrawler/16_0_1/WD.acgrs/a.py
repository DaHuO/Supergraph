numberOfCases = int(input())

for case in range(numberOfCases):
    v = int(input())
    if v == 0:
        print("Case #" + str(case + 1)  + ": INSOMNIA")
        continue

    allSeen = [False, False, False, False, False, False, False, False, False, False]

    i = 1
    while False in allSeen:
        n = v * i
        while n > 0:
            digit = n % 10
            n = n // 10

            allSeen[digit] = True

        if not(False in allSeen):
            print("Case #" +  str(case + 1)  + ": " + str(v * i))
            continue

        i = i + 1
