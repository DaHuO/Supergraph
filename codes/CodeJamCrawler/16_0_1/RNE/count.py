#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_int():
    return int(raw_input().strip())

if __name__ == '__main__':
    TARGET_DIGITS = (1<<10)-1
    DIGIT_MASKS = [1<<x for x in range(10)]
    T = get_int()
    # print T
    for case in range(T):
        N = get_int()
        # print N
        if N:
            all_digits = 0
            i = 0;
            while all_digits != TARGET_DIGITS:
                i += 1
                number = "{}".format(N * i)
                for digit in map(ord, number):
                    all_digits |= DIGIT_MASKS[digit-48]
            print("Case #{}: {}".format(case+1, N*i))
        else:
            print("Case #{}: INSOMNIA".format(case+1))

