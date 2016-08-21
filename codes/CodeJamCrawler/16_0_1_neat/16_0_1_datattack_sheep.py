from __future__ import print_function
import sys

line_ct = 1
N_cases = int(sys.stdin.readline())


while line_ct <= N_cases:
    prev_values = {}
    prev_digits = {}
    i = 1
    num = int(sys.stdin.readline())
    base = num

    while (True):
        if (prev_values.has_key(num)):
            print("Case #{}: INSOMNIA".format(line_ct))
            break
        
        prev_values[num] = 1

        for digit in set(str(num)):
            prev_digits[digit] = 1

        if (len(prev_digits) == 10):
            print("Case #{}: {}".format(line_ct, num))
            break
        
        i += 1
        num = base * i

    line_ct += 1