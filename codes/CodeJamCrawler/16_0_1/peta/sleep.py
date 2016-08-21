import sys
t = int(sys.stdin.readline())
for i in range(t):
    new_n = n = int(sys.stdin.readline())
    seen = [0 for x in range(10)]
    count = 0
    result = 0
    if n == 0:
        result = "INSOMNIA"
    else:
        while True:
            number = str(new_n)
            for digit in number:
                if seen[int(digit)] == 0:
                    seen[int(digit)] = 1
                    count += 1
            if count == 10:
                result = number
                break
            new_n = new_n + n
    print("Case #" + str(i+1) + ": " + result)
