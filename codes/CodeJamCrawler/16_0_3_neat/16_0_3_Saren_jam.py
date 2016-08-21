#!/usr/bin/env python3
from fractions import gcd
from subprocess import check_output

FORMAT = "Case #{}: {}"

def factor(n):
    return int(check_output(["factor", str(n)]).decode().split(": ")[1].split(" ")[0])

if __name__ == "__main__":
    input()
    n, j = input().split(" ")
    n, j = int(n), int(j)
    found = 0
    print("Case #1:")
    for i in range(1, 2 ** (n - 1), 2):
        jc = bin((1 << (n - 1)) + i)[2:]
        divisors = []
        jc_has_prime = False
        for base in range(2, 11):
            int_jc = int(jc, base)
            base_has_prime = True
            result = factor(int_jc)
            if result != int_jc:
                divisors.append(str(result))
                base_has_prime = False
            if base_has_prime:
                jc_has_prime = True
                break
        if not jc_has_prime:
            print(jc, " ".join(divisors))
            found += 1
            if found >= j:
                break
