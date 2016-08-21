""" LIMITS:
    for i in xrange(100):
        for j in xrange(100):
            do_something(i, j)
    Binary search
"""

import unittest
import sys
from collections import Counter

problem_name = 'A'
attempt = None
attempt = '1'
attempt = 'L'
# attempt = 'p'
# attempt = 'P'


class TestSolveIt(unittest.TestCase):

    def test(self):
        self.assertEqual("99999", solve_it("NINEENNNIENIINNINEEN"))
        self.assertEqual("1", solve_it("NOE"))
        self.assertEqual("012", solve_it("OZONETOWER"))
        self.assertEqual("2468", solve_it("WEIGHFOXTOURIST"))
        self.assertEqual("114", solve_it("OURNEONFOE"))
        self.assertEqual("3", solve_it("ETHER"))


def solve_it(letters):
    words = {
        0: "ZERO",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE"
    }
    output = {}
    letter_per_word = {}
    for number, word in words.iteritems():
        count_per_word = Counter()
        for letter in word:
            count_per_word[letter] += 1
        letter_per_word[number] = count_per_word

    input_letters = Counter()
    for letter in letters:
        input_letters[letter] += 1

    unique_letters = [
        (8, 'G'),
        (3, 'H'),
        (0, 'Z'),
        (2, 'T'),
        (4, 'R'),
        (6, 'X'),
        (1, 'O'),
        (5, 'F'),
        (7, 'V'),
        (9, 'I'),
    ]

    for number, letter in unique_letters:
        output[number] = input_letters[letter]
        for l in words[number]:
            input_letters[l] -= output[number]

    o_string = ""
    for i in range(10):
        o_string += str(i) * output[i]

    return o_string

    # possibilities = {}
    # for i in range(10):
    #     max_possible = sys.maxint
    #     for letter in letter_per_word[i]:
    #         if letter_per_word[i][letter]:
    #             max_possible = min(max_possible, input_letters[letter] / letter_per_word[i][letter])
    #     possibilities[i] = max_possible

    print possibilities

# MAIN


if __name__ == '__main__':
    if attempt is None:
        unittest.main()
    else:
        if attempt == 'L':
            file_name = '%s-large' % problem_name
        elif attempt == 'p':
            file_name = '%s-small-practice' % problem_name
        elif attempt == 'P':
            file_name = '%s-large-practice' % problem_name
        else:
            file_name = '%s-small-attempt%s' % (problem_name, attempt)
        dir_path = __file__.rsplit('/', 1)[0]

        with open('%s/%s.in' % (dir_path, file_name), 'r') as cases_in:
            with open('%s/%s.out' % (dir_path, file_name), 'w') as cases_out:
                total_cases = int(cases_in.next()[:-1])

                # NEXT LINES ARE SPECIFIC

                for case_number in xrange(total_cases):
                    letters = cases_in.next()[:-1]
                    out = solve_it(letters)
                    case_output = 'Case #%s: %s' % (case_number + 1, out)
                    print letters
                    print case_output
                    cases_out.write('%s\n' % case_output)
