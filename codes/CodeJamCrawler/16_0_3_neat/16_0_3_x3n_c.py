BASE_MIN = 2
BASE_MAX = 10
MAX_FACTOR = 5000

def lsb(n):
    pos = 0
    while n > 1:
        pos += 1
        n >>= 1
    return pos


def factor(n):
    k = 2
    while k < MAX_FACTOR and n % k != 0:
        k += 1

    if k == MAX_FACTOR or k == n:
        return -1
    else:
        return k


def mine(n, j):
    count = 0
    r = [x ** (n-1) + 1 for x in range(BASE_MIN, BASE_MAX + 1)]

    prev_code, k = 0, 1
    while count < j:
        code = k ^ (k >> 1)
        mask = code ^ prev_code
        is_addition = (code & mask != 0)
        pos = lsb(mask) + 1

        factors = [0] * (BASE_MAX - BASE_MIN + 1)

        for i in range(BASE_MAX - BASE_MIN + 1):
            if is_addition:
                r[i] += (i + BASE_MIN) ** pos
            else:
                r[i] -= (i + BASE_MIN) ** pos

            factors[i] = factor(r[i])

        prev_code = code
        k += 1

        if -1 in factors:
            continue

        count += 1
        yield [r[-1]] + factors


def main():
    t = int(input())

    for i in range(1, t + 1):
        n, j = [int(x) for x in input().split()]

        print(str.format("Case #{0}:", i))
        for ans in mine(n, j):
            print(' '.join(str(x) for x in ans))


if __name__ == '__main__':
    main()
