#!/usr/bin/env python3
"""
Getting the Digits
Code Jam 2016, Round 1B, Problem A

HOW TO USE:
#~: python a.py < input.in > output.out
"""

NAMES = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR",
         5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}
LETTERS = "ZEROONETWOTHREEFOURFIVESIXSEVENEIGHTNINE"


def decrypt_phone(phone_str):
    """decrypt phone number from S"""
    occurances = {letter: 0 for letter in set(LETTERS)}
    for letter in phone_str:
        occurances[letter] += 1

    digits = {x: 0 for x in range(10)}

    # ZERO
    current_digit = 0
    digits[current_digit] = occurances["Z"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # TWO
    current_digit = 2
    digits[current_digit] = occurances["W"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # FOUR
    current_digit = 4
    digits[current_digit] = occurances["U"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # FIVE
    current_digit = 5
    digits[current_digit] = occurances["F"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # SIX
    current_digit = 6
    digits[current_digit] = occurances["X"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # SEVEN
    current_digit = 7
    digits[current_digit] = occurances["V"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # EIGHT
    current_digit = 8
    digits[current_digit] = occurances["G"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # NINE
    current_digit = 9
    digits[current_digit] = occurances["I"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # ONE
    current_digit = 1
    digits[current_digit] = occurances["O"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    # THREE
    current_digit = 3
    digits[current_digit] = occurances["R"]
    for letter in NAMES[current_digit]:
        occurances[letter] -= digits[current_digit]

    return "".join(str(digit) * digits[digit] for digit in range(10))


def handle_case():
    """Handle the IO of the case, and return the answer"""
    given_str = input()
    result = decrypt_phone(given_str)

    return result


def handle_result(result):
    """Parse the result into the required format"""
    return result


def main():
    """Get the number of cases, solve each case and print its result"""
    num_of_tests = int(input())

    # iterate over test cases
    for test_case in range(1, num_of_tests + 1):
        result = handle_case()
        printable_result = handle_result(result)
        print("Case #{}: {}".format(test_case, printable_result))


if __name__ == "__main__":
    main()
