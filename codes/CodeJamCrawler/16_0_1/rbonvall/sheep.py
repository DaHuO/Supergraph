#!python3

def main():
    T = int(input())
    for t in range(T):
        n = int(input())
        print("Case #{}: {}".format(t + 1, solve(n)))

def solve(n):
    if n == 0:
        return 'INSOMNIA'
    digits = set(range(10))
    i = 0
    while digits:
        i += 1
        m = i * n
        while m:
            digits.discard(m % 10)
            m //= 10
    return i * n

main()
