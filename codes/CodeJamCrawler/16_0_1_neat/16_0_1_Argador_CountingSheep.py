digitCounter = [10]

for case in range(int(input())):
    num = int(input())
    digitCounter.clear();
    if num == 0:
        print("Case #" + str(case + 1) + ": INSOMNIA")
    else:
        i = num;
        while True:
            for digit in str(num):
                if digitCounter.count(digit) == 0:
                    digitCounter.append(digit)
            if len(digitCounter) == 10:
                break
            num += i
        print("Case #" + str(case + 1) + ": " + str(num))