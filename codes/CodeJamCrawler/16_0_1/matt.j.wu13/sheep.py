t = int(input())

def solve(n):
    if n == 0:
        return "INSOMNIA"
    mult = 0
    digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    def checkDigits(num):
        if num > 0:
            digits[num % 10] = 1
            checkDigits(num // 10)
    while True:
        mult += 1
        checkDigits(n * mult)
        flag = True
        for j in range(10):
            if digits[j] == 0:
                flag = False
                break
        if flag:
            return mult * n

for i in range(1, t + 1):
    n = int(input())
    solution = solve(n)
    print("Case #{}: {}".format(i, solution))
