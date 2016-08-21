def run():
    with open("input.txt") as f:
        numTestCases = 0
        numTestCase = 0
        for line in f:
            line = line.strip()
            if not numTestCases:
                numTestCases = int(line)
            else:
                numTestCase += 1
                testCase = int(line)
                asleep = False
                counter = 1
                cache = {}
                while not asleep:
                    number = counter*testCase
                    if number == 0:
                        print "Case #%s: INSOMNIA"%(numTestCase)
                        break
                    for n in list(str(number)):
                        cache[n] = True
                    if len(cache.keys()) == 10:
                        asleep = True
                        print "Case #%s: %s"%(numTestCase, number)
                    counter += 1

if __name__ == "__main__":
    run()