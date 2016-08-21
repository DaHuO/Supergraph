#!/usr/bin/env python3

def solver(multiplicand):
    if multiplicand == 0:
        return "INSOMNIA"
    
    multiplier = 1
    digits_found = [False for i in range(10)]
    while True:
        product = multiplicand * multiplier
        digits = product
        while digits >= 1:
            digits_found[digits % 10] = True
            digits //= 10
        multiplier += 1
        if all(digits_found):
            return str(product)

cases = int(input())
for i in range(cases):
    result = solver(int(input()))
    print("Case #{}: {}".format(i + 1, result))
