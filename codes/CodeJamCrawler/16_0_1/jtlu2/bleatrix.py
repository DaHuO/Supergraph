numInputs = int(input())
for lineNumber in range(1, numInputs + 1):
    n = int(input())
    originalN = n
    digitsSeen = dict.fromkeys(range(0, 10))
    numbersSeen = set()
    found = False
    while n not in numbersSeen:
        digits = str(n)
        for digit in digits:
            digitsSeen[int(digit)] = True
        numbersSeen.add(n)
        if None not in digitsSeen.values():
            print("Case #" + str(lineNumber) + ": " + str(n))
            found = True
            break
        n += originalN
    if found:
        continue
    print("Case #" + str(lineNumber) + ": INSOMNIA")