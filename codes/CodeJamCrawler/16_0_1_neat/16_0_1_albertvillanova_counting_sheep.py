#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Execute:
# python3 this_file.py < input.in > output.out

def solve(n):
    if n == 0:
        result = 'INSOMNIA'
    else:
        i = 1
        next = n
        seen_digits = set(list(str(next)))
        while len(seen_digits) < 10:
            i += 1
            next = i * n
            digits = set(list(str(next)))
            seen_digits.update(digits)
        result = next
    return result

if __name__ == "__main__":
    T = int(input())
     
    for i_test_case in range(T):
        N = int(input())
        solution = solve(N)
        print("Case #{}: {}".format(i_test_case + 1, solution))

