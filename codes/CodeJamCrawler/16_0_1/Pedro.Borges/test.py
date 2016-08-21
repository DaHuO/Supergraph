from sys import stdin

num_cases = int(stdin.readline()) + 1

for case in range(1, num_cases):
    num = int(stdin.readline())
    if num == 0:
        result = "INSOMNIA"
    else:
        current = num
        digits = set()
        while True:
            digits.update(set(str(current)))
            if len(digits) == 10:
                break
            current += num
        result = str(current)
    print("Case #" + str(case) + ": " + result)
    