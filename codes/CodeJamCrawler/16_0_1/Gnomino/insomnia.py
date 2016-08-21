nbTests = int(input())
for i in range(1, nbTests+1):
    n = int(input())
    currentN = n
    if n < 1:
        print("Case #" + str(i) + ": INSOMNIA")
        continue
    seenDigits = set()
    while len(seenDigits) < 10:
        s = str(currentN)
        for c in s:
            seenDigits.add(c)
        currentN += n
    print("Case #" + str(i) + ": " + str(currentN-n))
