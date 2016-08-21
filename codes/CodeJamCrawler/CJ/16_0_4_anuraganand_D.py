import sys

def solve():
    k, c, s = map(int, input().strip().split())
    size = k ** (c - 1)
    for i in range(0, k):
        print(1 + i * size, end = ' ')
        print(1 + i * size, end = ' ', file = sys.stderr)
    print()
    print(file = sys.stderr)

def main():
    test_cases = int(input().strip())
    for test_id in range(1, test_cases + 1):
        print('Case #{}: '.format(test_id), end = '')
        print('Case #{}: '.format(test_id), end = '', file = sys.stderr)
        solve()

if __name__ == '__main__':
    main()
