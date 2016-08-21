with open('B-large.in') as f:
    with open('B.out', 'w') as out:
        tests = f.readline()
        testNum = 1
        for line in f:
            flips = 0
            done = False
            pancakes = line
            while not done:
                last = pancakes.rfind("-")
                if last < 0:
                    done = True
                else:
                    first = pancakes.find("-")
                    if first == 0:
                        pancakes2 = pancakes[:last+1]
                        pancakes2 = pancakes2[::-1]
                        pancakes2 = pancakes2.replace("-", "0")
                        pancakes2 = pancakes2.replace("+", "-")
                        pancakes2 = pancakes2.replace("0", "+")
                        pancakes = pancakes2 + pancakes[last+1:]
                        flips += 1
                    else:
                        pancakes = pancakes.replace("+", "-", first)
                        flips += 1
            out.write("Case #" + str(testNum) + ": " + str(flips) + "\n")
            testNum += 1