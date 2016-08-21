# -*- coding: utf-8 -*-


def main():
    t = int(input())
    for case in range(1, t + 1):
        s = input()

        happy = '+' * len(s)
        blank = '-' * len(s)

        if s == happy:
            print('Case #{}: {}'.format(case, 0))
            continue
        if s == blank:
            print('Case #{}: {}'.format(case, 1))
            continue

        l = [c for c in s]
        cnt = 0
        i = 1
        while True:
            if l[i - 1] == l[i]:
                i += 1
            else:
                flip(l, i)
                cnt += 1
            if ''.join(l) == happy:
                print('Case #{}: {}'.format(case, cnt))
                break
            if ''.join(l) == blank:
                print('Case #{}: {}'.format(case, cnt + 1))
                break


def flip(l, n):
    for k in range(n):
        if l[k] == '+':
            l[k] = '-'
        else:
            l[k] = '+'
    i, j = 0, n - 1
    while i < j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    main()
