from __future__ import print_function

import fractions
import sys

digits_strings = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
unique_seq = [('Z', 0), ('U', 4), ('W', 2), ('O', 1), ('X', 6), ('R', 3), ('T', 8), ('S', 7), ('F', 5), ('I', 9)]

def chr2idx(ch):
    return ord(ch) - ord('A')

def idx2chr(idx):
    return  chr(ord('A') + idx)

def calc(S):
    counts = [0] * 26
    for ch in S:
        counts[chr2idx(ch)] += 1

    out = [0] * 10

    for ch, digit in unique_seq:
        ch_pos = chr2idx(ch)
        num_digit = counts[ch_pos]
        if num_digit > 0:
            out[digit] = num_digit
            for x in digits_strings[digit]:
                x_pos = chr2idx(x)
                counts[x_pos] -= num_digit
                assert counts[x_pos] >= 0, '{}: {} {} {} {}'.format(S, ch, digit, x, counts[x_pos])

    r = ''
    for i, n in enumerate(out):
        r += str(i) * n
    return r

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        s = f.readline().strip()

        r = calc(s)

        print(str.format('Case #{}: {}', case_id, r))

def test1():
    print(sum([len(x) for x in digits_strings]))
    chars_set = set()
    for x in digits_strings:
        chars_set.update(set(x))
    print(chars_set, len(chars_set))

if __name__ == '__main__':
    main()
    # test1()

