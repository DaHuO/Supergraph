import sys

INPUT_FILE_NAME = 'input.in'
OUTPUT_FILE_NAME = 'out'

sys.stdin = open(INPUT_FILE_NAME)
sys.stdout = open(OUTPUT_FILE_NAME, 'w')

def is_prime(n):
    n = abs(int(n))
    if n < 2:
        return 0
    if n == 2:
        return 0
    if not n & 1:
        return 2
    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return x
    return 0

def base_n(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

print("Case #1:")

cnt = 0
for cand in range(1 << 15, 1 << 16):
    base2 = base_n(cand, 2)
    if base2[0] == '1' and base2[15] == '1':
        n = int(base2)
        res = [0] * 11
        res[1] = n
        res[2] = is_prime(cand)
        res[10] = is_prime(n)
        ok = False
        if res[2] != 0 and res[10] != 0:
            ok = True
            for i in range(3, 10):
                res[i] = is_prime(int(base2, i))
                if res[i] == 0:
                    ok = False
                    break
        if ok:
            line = ''
            for i in range(1, 11):
                line += str(res[i]) + ' '
            print(line)
            cnt += 1
            if cnt == 50:
                break
