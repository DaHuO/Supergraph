#!/usr/bin/env python3


def compute(n):
    if n == 0:
        return None
    digits_left = set('0123456789')
    for i in range(n, max(1000, n*n), n):
        digits_left.difference_update(str(i))
        if not digits_left:
            return i


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n = int(input())
        answer = compute(n)
        if answer is None:
            answer = 'INSOMNIA'
        print('Case #{}: {}'.format(case, answer))
