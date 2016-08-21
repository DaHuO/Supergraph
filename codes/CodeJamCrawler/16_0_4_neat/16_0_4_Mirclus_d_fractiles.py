#! /usr/bin/env python3
import sys


def d_fractile(length, generation, students):
    # Note: if length == students (small problem), just output range (1...length)

    # General:
    # needed: ceil(length / generation) > students
    if (generation == 1 and length > students) or\
            (generation > 1 and (length + 1) // generation > students):
        return "IMPOSSIBLE"

    # We need positions that are influenced by every position in the input
    cur_gen = 0
    necessary_positions = [x for x in range(length)]
    cur_idx = 0

    result = []
    while necessary_positions:
        if cur_gen == generation:
            result.append(cur_idx)
            cur_gen = 0
            cur_idx = 0
        cur_idx *= length
        cur_idx += necessary_positions.pop(0)
        cur_gen += 1

    while cur_gen < generation:
        cur_idx *= length
        cur_gen += 1

    result.append(cur_idx)
    return " ".join([str(i + 1) for i in result])


def main():
    test_cases = int(sys.stdin.readline())

    for test_case in range(test_cases):
        values = [int(x) for x in sys.stdin.readline().split(" ")]
        print("Case #{}: {}".format(test_case + 1, d_fractile(*values)))


if __name__ == "__main__":
    main()
