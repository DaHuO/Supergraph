"""
Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep
faster. First, she picks a number N. Then she starts naming N, 2 x N, 3 x N,
and so on. Whenever she names a number, she thinks about all of the digits in
that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9)
she has seen at least once so far as part of any number she has named. Once she
has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) x N directly after i x
N. For example, suppose that Bleatrix picks N = 1692. She would count as
follows:

    N = 1692. Now she has seen the digits 1, 2, 6, and 9.
    2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
    3N = 5076. Now she has seen all ten digits, and falls asleep.

What is the last number that she will name before falling asleep? If she will
count forever, print INSOMNIA instead.
"""
import argparse

def count_sheep(N):
    """Last number before Bleatrix falls asleep.

    >>> count_sheep(0)
    'INSOMNIA'
    >>> count_sheep(1692)
    5076
    """
    if N == 0:
        # In any other case, you will reach all the numbers.
        return 'INSOMNIA'
    digits_seen = set()
    current_count = N
    while True:
        digits_seen.update(list(str(current_count)))
        if len(digits_seen) == 10:
            break
        current_count += N
    return current_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input_file')
    parser.add_argument('output_file')

    args = parser.parse_args()
    counts = []
    with open(args.input_file) as f:
        next(f) # Ignore number of test cases.
        for line in f:
            counts.append(count_sheep(int(line)))
    with open(args.output_file, 'wb') as f:
        for i, count in enumerate(counts):
            f.write('Case #{}: {}\n'.format(i + 1, count))
