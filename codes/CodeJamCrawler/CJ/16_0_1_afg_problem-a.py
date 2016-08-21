#!/usr/bin/env python3

def search(casenum, base):
    print('Case #{}: '.format(casenum), end='')
    if base == 0:
        print('INSOMNIA')
        return
    seen = set()
    factor = 0
    while len(seen) < 10:
        factor += 1
        seen.update(str(factor * base))
    print(factor * base)

for case_number in range(int(input())):
    search(case_number + 1, int(input()))
