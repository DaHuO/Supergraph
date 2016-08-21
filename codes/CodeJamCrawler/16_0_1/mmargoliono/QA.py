import sys

def split(n):
    unique = set()
    for c in str(n):
        unique.add(c)
    return unique

def calculate(n):
    if n == 0:
        return "INSOMNIA"
    unique = set()
    multiplier = 0
    while len(unique) < 10:
        multiplier += 1
        unique.update(split(multiplier * n))
    return str(multiplier * n)

n = (int) (sys.stdin.readline().strip())
for i in range (1, n+1):
    number = int(sys.stdin.readline().strip())
    print("Case #{}: {}".format(i, calculate(number)))
