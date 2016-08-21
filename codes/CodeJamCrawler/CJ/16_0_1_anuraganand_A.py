import sys

def get_last(n):
    seen = set()
    x = n
    while True:
        for c in str(x):
            seen.add(c)
        if len(seen) == 10:
            return x
        x += n

def solve(test_id):
    n = int(input().strip())
    if n == 0:
        print('Case #{}: INSOMNIA'.format(test_id))
        print('Case #{}: INSOMNIA'.format(test_id), file = sys.stderr)
        return
    ans = get_last(n)
    print('Case #{}: {}'.format(test_id, ans))
    print('Case #{}: {}'.format(test_id, ans), file = sys.stderr)

def main():
    test_cases = int(input().strip())
    for test_id in range(1, test_cases + 1):
        solve(test_id)

def check():
    for n in range(1, int(1e6) + 1):
        print('{} -> {}'.format(n, get_last(n)))

if __name__ == '__main__':
    main()
    # check()
