import sys
import multiprocessing
from collections import deque


def pancake_sort(start):
    q = deque([(start, 0)])
    min_flips = {start: 0}
    best = sum(k == '-' for k in start) * 3
    while q:
        cakes, c = q.popleft()
        # print cakes, c
        if c >= best:
            continue
        for i in range(len(cakes)):
            if i == len(cakes) - 1 or (cakes[0] == cakes[i] and cakes[i] != cakes[i+1]):
                flipped_cakes = ''.join('+' if k == '-' else '-' for k in cakes[:i+1]) + cakes[i+1:]
                # print cakes[:i+1], ''.join('+' if k == '-' else '+' for k in cakes[:i+1])
                # print "i", i, flipped_cakes
                if flipped_cakes not in min_flips or min_flips[flipped_cakes] > c + 1:
                    min_flips[flipped_cakes] = c + 1
                    q.append((flipped_cakes, c + 1))
                if all(k == '+' for k in flipped_cakes):
                    best = c + 1
    return best


def main():
    T = int(sys.stdin.readline())
    inputs = [sys.stdin.readline().strip() for _ in range(T)]
    cores = multiprocessing.cpu_count() / 2
    p = multiprocessing.Pool(cores)
    outputs = p.map(pancake_sort, inputs)
    for t, c in enumerate(outputs):
        print "Case #%d: %d" % (t + 1, c)


if __name__ == '__main__':
    main()
