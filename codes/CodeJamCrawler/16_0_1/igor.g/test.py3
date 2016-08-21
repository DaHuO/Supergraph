#!/usr/bin/env python3
import sys

def solve(num):
    if num == 0:
        return "INSOMNIA"

    seen = [0] * 10

    i = 1
    while True:
        n = num * i
        while n:
            d = n % 10
            if seen[d] == 0:
                seen[d] = 1
            n //= 10
    
        if sum(seen) == 10:
            return num * i
        i += 1

def main(filename):
    with open(filename, 'r') as f:
        testcases = int(f.readline())
        for case_num in range(testcases):
            print("Case #{0}: {1}".format(
                case_num + 1,
                solve(int(f.readline()))))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
