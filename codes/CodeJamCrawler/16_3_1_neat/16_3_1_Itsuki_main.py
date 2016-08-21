#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from heapq import heappush, heappop


def solve(n, parties):
    heap = []
    result = ''
    count = 0
    for i, num in enumerate(parties):
        heappush(heap, (1000 - num, chr(ord('A') + i)))
    while len(heap) > 0:
        item = heappop(heap)
        result += item[1]
        count += 1
        if item[0] < 999:
            newItem = (item[0] + 1, item[1])
            heappush(heap, newItem)
        if count % 2 == 0 and len(heap) > 0:
            count = 0
            result += ' '
            continue
        rest = 0
        for item in heap:
            rest += (1000 - item[0])
            if rest > 2:
                break
        if rest == 2:
            count = 0
            result += ' '
    return result


if __name__ == '__main__':
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        n = int(input())
        parties = [int(s) for s in input().split(' ')]
        print('Case #{}: {}'.format(t, solve(n, parties)))
