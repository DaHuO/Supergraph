#!/usr/bin/python

def solve(number):
    if number == 0:
        return 'INSOMNIA'
    seen = set()
    multiplier = 1
    seen.update([c for c in str(number)])
    while len(seen) < 10:
       multiplier += 1
       seen.update([c for c in str(number * multiplier)])
    return number * multiplier


def main():
    t = int(input())
    for i in range(1, t + 1):
        start = int(input().strip())
        print('Case #{}: {}'.format(i, solve(start)))


if __name__ == '__main__':
    main()
