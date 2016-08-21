t = int(input())

for i in range(t):
    n = input()

    if int(n) == 0:
        print("Case #" + str(i + 1) + ": INSOMNIA")
        continue
    m = n
    a = 1

    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    while True:
        if digits:
            m = str(int(n) * a)
            for c in list(m):
                if c in digits:
                    digits.remove(c)
            a += 1
        else:
            print("Case #" + str(i + 1) + ": " + m)
            break
