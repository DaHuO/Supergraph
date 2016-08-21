#!/usr/bin/python2
# -*- coding: utf8 -*-
# Google Code Jam 2016 - Qualification Round - Problem A - Mateusz Kurek


def main():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        if n == 0:
            result = 'INSOMNIA'
        else:
            digits = set(str(n))
            val = n
            while(len(digits) < 10):
                val += n
                digits.update(set(str(val)))
            result = val
        print('Case #{}: {}'.format(i, result))

if __name__ == '__main__':
    main()
