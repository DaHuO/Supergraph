from __future__ import print_function

import sys

try:
    input = raw_input
except NameError:
    pass


def find_tiles_direct_descendant(k, c, tile_idx):
    orig_tile_idx = tile_idx

    for __ in range(c - 1):
        tiles_in_preceding_segments = k * tile_idx
        tile_idx = tiles_in_preceding_segments + orig_tile_idx
        # (k + 1) * tile_idx

    return tile_idx


def main():
    num_cases = input()

    for case_idx, kcs in enumerate(iter(sys.stdin.readline, ''), 1):
        k, c, s = map(int, kcs.split())

        tiles_to_check = [(find_tiles_direct_descendant(k, c, ti) + 1)
                          for ti in range(k)]

        tiles_to_check_str = ' '.join(map(str, tiles_to_check))

        if s < k:
            # This won't happen with D-small, and isn't true anyway; I'm
            # just putting it here as a sort of placeholder.
            print("Case #{}: IMPOSSIBLE".format(case_idx))
        else:
            print("Case #{}: {}".format(case_idx, tiles_to_check_str))


if __name__ == '__main__':
    main()
