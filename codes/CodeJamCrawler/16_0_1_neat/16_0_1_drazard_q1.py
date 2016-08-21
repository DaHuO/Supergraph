from sys import stdin, exit

samples = [int(i) for i in stdin.readlines()]
numCases = samples.pop(0)
#for num in samples:
for num in samples:
    if num == 0:
        print("Case #" + str(samples.index(num) + 1) + ": INSOMNIA")
        continue
    originalNum = num
    currentNum = num
    seen = [i for i in range(10)]
    while num > 0:
        digit = (int)(num % 10)
        num -= digit
        num /= 10
        #print("Working on " + str(originalNum) + ", currently at " + str((int)(digit)))
        if digit in seen:
            seen.remove(digit)
        if len(seen) == 0:
            break
        elif num == 0:
            currentNum += originalNum
            num = currentNum
    print("Case #" + str(samples.index(originalNum) + 1) + ": " + str(currentNum))