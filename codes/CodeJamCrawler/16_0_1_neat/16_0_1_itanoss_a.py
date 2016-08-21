import sys
def read_int(): return int(sys.stdin.readline())

def calc(n):
    if n == 0:
        return "INSOMNIA"
    seen = [0 for x in range(10)]

    i = 1
    while True:
        for digit in str(i * n):
            seen[int(digit)] += 1
        if not [1 for x in seen if x == 0]:
            break
        i += 1

    return str(i*n)

T = read_int()

for t in range(T):
    print("Case #{}: {}".format(t+1, calc(read_int())))
