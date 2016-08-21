import math


def div(z):
    for d in range(2, int(math.sqrt(z)) + 1):
        if z % d == 0:
            return d
    else:
        return -1


with open("C-small-attempt0.in") as f:
    f.readline()
    nums = list(map(int, f.readline().strip().split()))
    n = nums[0]
    j = nums[1]

results = list()

for i in range(0, 2 ** (n - 2)):
    a = ((2 ** (n - 2) + i) << 1) + 1  # Make first and last digit 1
    num = bin(a)[2:]
    divisors = list()
    for k in range(2, 11):
        d = div(int(num, k))
        if d != -1:
            divisors.append(d)
        else:
            break
    else:
        results.append((num, divisors))

    if len(results) == j:
        break

with open("C-small-attempt0.out", "w") as f:
    f.write("Case #1:\n")
    for i in range(j):
        f.write(results[i][0] + " " + " ".join(map(str, results[i][1])) + "\n")
