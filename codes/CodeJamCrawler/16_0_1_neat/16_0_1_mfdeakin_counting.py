
def getDigits(n):
    digits = set()
    if n == 0:
        return {0}
    while n > 0:
        digits = digits.union({n % 10})
        n //= 10
    return digits

numTests = int(input())
for i in range(1, numTests + 1):
    n = int(input())
    print("Case #" + str(i) + ": ", end="")
    if n == 0:
        print("INSOMNIA")
        continue
    digits = set()
    k = 1
    while len(digits) < 10:
        digits = digits.union(getDigits(n * k))
        k += 1
    print(str((k - 1) * n))
