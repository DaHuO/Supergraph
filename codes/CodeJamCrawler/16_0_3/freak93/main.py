T = int(input())
print("Case #1:")

N, J = [int(x) for x in input().split()]

def check(x):
    for i in range(2, x):
        if i * i > x:
            break
        if x % i == 0:
            return i
    return None

ANSWER = []
for i in range(2 ** (N - 1) + 1, 2 ** N , 2):
    PRIME = False
    DIVS = []
    NUMBERS = []
    for base in range(2, 11):
        x = i
        y = 0
        while x > 0:
            y *= base
            if x % 2 == 1:
                y += 1
            x //= 2
        div = check(y)
        if div is None:
            PRIME = True
            break
        DIVS += [div]
        NUMBERS += [y]
    if not PRIME:
        J -= 1
        print("%s %s" %(bin(i)[2:][::-1], " ".join([str(x) for x in DIVS])))
    if J == 0:
        break

