with open("input.txt", "r") as inputFile:
    with open("output.txt", "w") as outputFile:
        inputFile.readline()
        count = 0
        for line in inputFile:
            count += 1 
            chars = list(line.rstrip('\n'))
            simulated = [chars[0]]
            for i in range(1, len(chars)):
                if chars[i] >= simulated[0]:
                    simulated.insert(0, chars[i])
                else:
                    simulated.append(chars[i])
            result = "".join(i for i in simulated)
            outputFile.write("Case #{}: {}\n".format(count, result))
