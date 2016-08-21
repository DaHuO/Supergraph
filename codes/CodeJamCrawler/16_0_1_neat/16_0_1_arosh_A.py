# coding: UTF-8

def solve(N):
    if N == 0:
        return 'INSOMNIA'
    num = N
    digits = set()
    while True:
        digits.update(*str(num))
        if len(digits) == 10:
            return num
        num += N

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        print('Case #{}: {}'.format(i + 1, solve(N)))

if __name__ == '__main__':
    main()
