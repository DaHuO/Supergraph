#!/usr/bin/env python
import argparse
import random


def main(infile, out):
    for line in read_input(infile, out):
        S = list(line)
        counts = {}
        digits = {
            '0': "ZERO",
            '1': "ONE",
            '2': "TWO",
            '3': "THREE",
            '4': "FOUR",
            '5': "FIVE",
            '6': "SIX",
            '7': "SEVEN",
            '8': "EIGHT",
            '9': "NINE",
        }
        for char in S:
            if counts.get(char):
                counts[char] += 1
            else:
                counts[char] = 1
        counts_orig = counts.copy()
        tries = 0
        while len(counts) > 0:
            counts = counts_orig.copy()
            number = []
            digit_order = sorted(digits)
            for digit in digit_order:
                digit_counts = {}
                for char in digits[digit]:
                    if digit_counts.get(char):
                        digit_counts[char] += 1
                    else:
                        digit_counts[char] = 1
                while all(counts.get(c, 0) >= digit_counts[c] for c in digits[digit]):
                    if tries > 0 and random.random() > 0.5:
                        break
                    number.append(digit)
                    for c in digits[digit]:
                        counts[c] -= 1
                        if counts[c] == 0:
                            del counts[c]
            tries += 1

        print(counts)
        out.write(''.join(number) + '\n')


def read_input(infile, out):
    with open(infile, 'r') as f:
        num_cases = int(f.readline())
        for case in range(1, num_cases+1):
            out.write('Case #{}: '.format(case))
            yield f.readline().rstrip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="codejam 1A")
    parser.add_argument('input', type=str,
                        help='Input file')
    parser.add_argument('output', type=argparse.FileType('w'),
                        help='Output file')
    args = parser.parse_args()
    main(args.input, args.output)
