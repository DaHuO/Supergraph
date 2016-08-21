from __future__ import print_function

import heapq
import sys

def idx2chr(idx):
    return  chr(ord('A') + idx)

def calc(nums):
    q = [(-x, i) for i, x in enumerate(nums)]
    heapq.heapify(q)
    r = []
    while q:
        action = ''
        x = heapq.heappop(q)
        action += idx2chr(x[1])
        if x[0] < -1:
            heapq.heappush(q, (x[0]+1, x[1]))
        if q:
            x = heapq.heappop(q)
            if len(q) == 1 and x[0] == -1:
                # Don't leave one group.
                heapq.heappush(q, x)
            else:
                action += idx2chr(x[1])
                if x[0] < -1:
                    heapq.heappush(q, (x[0]+1, x[1]))
        r.append(action)
    return r

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        N = int(f.readline().strip())
        nums = map(int, f.readline().strip().split())
        assert N == len(nums), '{} != {}'.format(N, len(nums))
        r = calc(nums)
        r_str = ' '.join(r)

        print(str.format('Case #{}: {}', case_id, r_str))

if __name__ == '__main__':
    main()
    # test1()

