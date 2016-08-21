#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        N = int(input())
        if N == 0:
            answer = "INSOMNIA"
        else:
            get_digits = lambda x: [int(d) for d in str(x)]
            seen_digits = [False] * 10

            current_number = N
            while (not all(seen_digits)):
                digits = get_digits(current_number)
                for d in digits:
                    seen_digits[d] = True
                current_number += N
            answer = current_number - N

        print("Case #{0}: {1}".format(case + 1, answer))
