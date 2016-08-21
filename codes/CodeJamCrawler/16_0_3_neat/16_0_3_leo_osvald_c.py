#!/usr/bin/env python3

from itertools import islice
import sys

def find_divisor(x, prune_threshold):
    d = 2
    d2_max = min(prune_threshold, x)
    while d * d <= d2_max:
        if x % d == 0:
            return d
        d += 1
    return 0

def solve(n, prune_threshold):
    n -= 2
    bases = tuple(range(2, 11))
    hi_lo_mask = (1 << (n + 1)) | 1
    ds = []
    for bits in range(1 << n):
        bits = (bits << 1) | hi_lo_mask
        bits_str = bin(bits)[2:]
        for base in bases:
            x = int(bits_str, base)
            d = find_divisor(x, prune_threshold)
            if not d: break
            ds.append(d)
        if len(ds) == 9:
            yield bits_str, ds
        del ds[:]

def main(args=sys.argv):
    t = int(sys.stdin.readline())
    for i in range(t):
        n, count = tuple(map(int, sys.stdin.readline().rstrip().split(" ")))
        print("Case #%d:" % (i + 1))

        gen_atmost_count = lambda: islice(solve(n, prune_threshold), count)
        for prune_threshold_log10 in range(2, n + 1):
            prune_threshold = 10 ** prune_threshold_log10
            gen_count = len(list(gen_atmost_count()))
            if gen_count == count:
                for bits, divs in gen_atmost_count():
                    print(bits, " ".join(map(str, divs)))
                break
            # else:
            #     print("prune=", prune_threshold, "found=", gen_count, file=sys.stderr)

    return 0

if __name__ == '__main__': sys.exit(main())
