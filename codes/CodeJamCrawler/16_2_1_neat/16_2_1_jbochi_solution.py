from collections import defaultdict
from pprint import pprint
import sys

numbers_letters = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
"SIX", "SEVEN", "EIGHT", "NINE"]

order = [
    ('Z', 0), ('W', 2), ('U', 4), ('X', 6), ('G', 8),
    ('T', 3), ('O', 1), ('F', 5), ('S', 7), ('N', 9)
]


def count_letters(letters):
    h = defaultdict(int)
    for letter in letters:
        h[letter] += 1
    # print letters, h
    return h

number_letters_hash = [count_letters(l) for l in numbers_letters]

def remove_number(letters_count, number):
    for letter, count in number_letters_hash[number].items():
        letters_count[letter] -= count


def output(letters):
    letters_count = count_letters(letters)
    # print letters, letters_count
    phone_number = ""
    for letter_to_remove, number in order:
        while letters_count[letter_to_remove] > 0:
            phone_number += str(number)
            remove_number(letters_count, number)
    # print letters_count
    assert all(x == 0 for x in letters_count.values())
    return ''.join(sorted(phone_number))


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        letters = sys.stdin.readline().strip()
        answer = output(letters)
        print "Case #%d: %s" % (t + 1, answer)
