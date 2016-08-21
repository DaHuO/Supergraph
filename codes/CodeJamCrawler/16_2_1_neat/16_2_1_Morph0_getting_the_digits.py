import string

NUMBER_OR_LETTERS = len(string.ascii_uppercase)
DIGITS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]


def pre_solve(input_string):
    counter_list = [0] * NUMBER_OR_LETTERS
    for i in input_string:
        char_index = ord(i) - ord('A')
        counter_list[char_index] += 1
    return counter_list

DIGITS_PRICE = [pre_solve(i) for i in DIGITS]


class PriceException(Exception):
    pass


def subtract(left, arr2):
    left_copy = left[:]
    for i in xrange(NUMBER_OR_LETTERS):
        left_copy[i] -= arr2[i]
        if left_copy[i] < 0:
            raise PriceException("pasten")
    return left_copy


def find_number_rec(first_digit, letters_count):
    if not any(letters_count):
        return ""
    for i in xrange(first_digit, 10):
        try:
            new_count = subtract(letters_count, DIGITS_PRICE[i])
            partial_solution = "%d%s" % (i, find_number_rec(i, new_count))
            return partial_solution
        except PriceException:
            continue
    raise PriceException("failure")


def solve(input_string):
    letters_count = pre_solve(input_string)
    solution = find_number_rec(0, letters_count)
    return solution


with open("getting_the_digits.in") as fin:
    T = int(fin.readline())
    for t in xrange(T):
        S = fin.readline().strip()
        print "Case #%d: %s" % (t+1, solve(S))