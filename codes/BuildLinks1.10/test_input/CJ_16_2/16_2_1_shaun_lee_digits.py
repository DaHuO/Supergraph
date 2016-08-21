from __future__ import print_function
import sys

# 7 9
numbers_r = ["ONE", "THREE", "FIVE", "SEVEN", "NINE"]

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
           "SEVEN", "EIGHT", "NINE"]

def read_input(in_file):
    in_file.seek(0, 2)
    end = in_file.tell()
    in_file.seek(0)
    T = int(in_file.readline().strip())
    while in_file.tell() < end:
        result = in_file.readline().strip()
        yield result


def delete_word(letters, word):
    for i in range(len(word)):
        letters.remove(word[i])


def unique_letters():
    letters = set("".join(numbers_r))
    for x in letters:
        if len([1 for y in numbers_r if x in y]) == 1:
            print(x)


def check_case(S):
    result = []
    letters = list(S)
    # find zeros
    zeros = ["0" for x in letters if x == "Z"]

    for i in range(len(zeros)):
        delete_word(letters, "ZERO")
    result += zeros

    # find sixes
    sixes = ["6" for x in letters if x == "X"]
    for i in range(len(sixes)):
        delete_word(letters, "SIX")
    result += sixes

    # find eights
    eights = ["8" for x in letters if x == "G"]
    for i in range(len(eights)):
        delete_word(letters, "EIGHT")
    result += eights

    # find fours
    fours = ["4" for x in letters if x == "U"]
    for i in range(len(fours)):
        delete_word(letters, "FOUR")
    result += fours

    # find twos
    twos = ["2" for x in letters if x == "W"]
    for i in range(len(twos)):
        delete_word(letters, "TWO")
    result += twos

    # find fives
    fives = ["5" for x in letters if x == "F"]
    for i in range(len(fives)):
        delete_word(letters, "FIVE")
    result += fives

    # find threes
    threes = ["3" for x in letters if x == "H"]
    for i in range(len(threes)):
        delete_word(letters, "THREE")
    result += threes

    # find ones
    ones = ["1" for x in letters if x == "O"]
    for i in range(len(ones)):
        delete_word(letters, "ONE")
    result += ones

    # find sevens
    sevens = ["7" for x in letters if x == "V"]
    for i in range(len(sevens)):
        delete_word(letters, "SEVEN")
    result += sevens

    # find nines
    nines =  ["9" for x in letters if x == "I"]
    for i in range(len(nines)):
        delete_word(letters, "NINE")
    result += nines

    return "".join(sorted(result))


def main():
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for S in read_input(input_file):
            case_no += 1
            print("Case #" + str(case_no) + ": " + check_case(S))

if __name__ == '__main__':
    main()
