def sheepCount(file):

    f = open(file)

    numCases = 0

    testCases = []

    for i, line in enumerate(f):

        if i == 0:
            numCases = int(line)

        else:
            seenNums = []

            N = int(line)

            if N == 0:
                testCases.append("INSOMNIA")

            else:

                multiplier = 1
                modNum = N * multiplier

                while 1:

                    for ch in str(modNum).strip():
                        if ch not in seenNums:
                            seenNums.append(ch)

                    if len(seenNums) == 10:
                        testCases.append(str(modNum))
                        break

                    else:
                        multiplier += 1
                        modNum = N * multiplier


    f.close()

    fp = open("newLarge", 'a')

    iteration = 1
    for item in testCases:
        fp.write("Case #" + str(iteration) + ": " + item + "\n")
        iteration += 1

    fp.close()

sheepCount("A-large.in")






