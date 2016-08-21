with open("A-large.in") as f:
    t = int(f.readline().strip("\n"))
    digitDict = {}
    answers = []

    for i in range(t):
        n = int(f.readline().strip("\n"))
        initial_n = n
        if n == 0:
            answers.append("INSOMNIA")
            continue
        for i in range(10):
            digitDict[str(i)] = 0
        count = 1
        while True:
            breakflag = True
            for digit in list(str(n)):
                digitDict[digit] = digitDict[digit] + 1
            for digit in digitDict:
                if digitDict[digit] == 0:
                    breakflag = False
                    break

            if breakflag:
                break

            count = count + 1
            n = initial_n*count
        answers.append(n)

    for i in range(len(answers)):
        print("Case #" + str(i+ 1) + ": " + str(answers[i]))