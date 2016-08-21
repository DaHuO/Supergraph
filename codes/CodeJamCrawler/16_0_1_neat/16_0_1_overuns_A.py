# -*- coding: utf-8 -*-


def main():
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        if n == 0:
            print('Case #{}: {}'.format(case, 'INSOMNIA'))
            continue
        digits = set()
        iter = 1
        while True:
            m = n * iter
            while m:
                digit = m % 10
                digits.add(digit)
                m = m // 10
            if len(digits) == 10:
                print('Case #{}: {}'.format(case, n * iter))
                break
            iter += 1


if __name__ == "__main__":
    main()
