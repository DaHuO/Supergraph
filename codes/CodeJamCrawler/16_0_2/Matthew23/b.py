#!/usr/bin/python3
# -*- coding: utf8 -*-
# Google Code Jam 2016 - Qualification Round - Problem B - Mateusz Kurek


def main():
    t = int(input())
    for i in range(1, t+1):
        s = input()
        l = [s[0]]
        for c in s[1:]:
            if l[-1] != c:
                l.append(c)
        # any_plus = any([c == '+' for c in l])
        result = len(l) - 1
        if l[-1] == '-':
            result += 1
        print('Case #{}: {}'.format(i, result))

if __name__ == '__main__':
    main()
