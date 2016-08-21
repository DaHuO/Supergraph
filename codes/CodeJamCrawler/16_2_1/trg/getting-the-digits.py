import sys
from collections import Counter
from itertools import combinations_with_replacement


digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
digit_counters = {i: Counter(digits[i]) for i in range(10)}


def is_counter_subset(a, b):
    for k, v in a.items():
        if v > b[k]:
            return False
    return True


def seq_match(digit_seq, letters_counter):
    cnt = Counter()
    for digit in digit_seq:
        cnt += digit_counters[digit]
        if not is_counter_subset(cnt, letters_counter):
            break
    return cnt == letters_counter


def find_matching_digits(letters_counter):
    return [i for i in range(10)
            if is_counter_subset(digit_counters[i], letters_counter)]


def find_seq(letters_counter):
    num_of_letters = sum(letters_counter.values())
    digits = find_matching_digits(letters_counter)
    for seq_len in range(num_of_letters // 5, num_of_letters // 3 + 1):
        for digit_seq in combinations_with_replacement(digits, seq_len):
            if seq_match(digit_seq, letters_counter):
                return digit_seq

    raise ValueError('should not happen')


def main():
    line_iter = iter(sys.stdin)
    T = int(next(line_iter))

    for i in range(T):
        cnt = Counter(next(line_iter).strip())
        seq = find_seq(cnt)
        print('Case #{0}: {1}'.format(i + 1, ''.join(str(d) for d in seq)))


if __name__ == '__main__':
    main()
