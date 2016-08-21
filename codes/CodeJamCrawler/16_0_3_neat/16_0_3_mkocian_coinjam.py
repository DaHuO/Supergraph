T = int(input().strip())

N, J = map(int, input().split())

def divisor(x):
    if x % 2 == 0:
        return 2
    i = 3
    while i < 500:
        if x % i == 0:
            return i
        i += 2
    return None

def to_base(x, n):
    return int(bin(x)[2:], n)

bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]

coinjams = {}
a = '1' + (N-2) * '0' + '1'
b = '1' * N
for x in reversed(range(int(a, 2), int(b, 2), 2)):
    divs = []
    for b in bases:
        d = divisor(to_base(x, b))
        if d is not None:
            divs.append(d)
    if len(divs) == len(bases):
        coinjams[x] = divs
    if len(coinjams) == J:
        break

print("Case #1:")
for k, v in coinjams.items():
    print(bin(k)[2:], " ".join(map(str, v)))
