#!/usr/bin/env python

T = int(raw_input().strip())

def flip(happies, n):
    return [not(x) for x in happies[:n]] + happies[n:]

assert flip([True, False, True], 0) == [True, False, True]
assert flip([True, False, True], 2) == [False, True, True]

for i in range(1, T+1):
    print ("Case #%d:" % i),
    happies = [x == '+' for x in raw_input().strip()]
    ans = 0
    while not all(happies):
        ans += 1
        counter = 0
        looking_for = happies[0]
        for x in happies:
            if x == looking_for:
                counter += 1
            else:
                break
        happies = flip(happies, counter)
    print(ans)
