#!/usr/bin/python

def get_digits(number_jumble):
    '''
    You just made a new friend at an international puzzle conference,
    and you asked for a way to keep in touch. You found the following
    note slipped under your hotel room door the next day:

    "Salutations, new friend! I have replaced every digit of my phone
    number with its spelled-out uppercase English representation
    ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN",
    "EIGHT", "NINE" for the digits 0 through 9, in that order), and
    then reordered all of those letters in some way to produce a
    string S. It's up to you to use S to figure out how many digits
    are in my phone number and what those digits are, but I will tell
    you that my phone number consists of those digits in nondecreasing
    order. Give me a call... if you can!"

    You would to like to call your friend to tell him that this is
    an obnoxious way to give someone a phone number, but you need
    the phone number to do that! What is it?
    :param start_word: input string containing mixed up
    characters of number representation of phone number
    :return: phone_number_string: integer representation of phone number
    '''
    number_digits_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    number_jumble = list(number_jumble)

    while 'Z' in number_jumble:
        number_jumble.remove('Z')
        number_jumble.remove('E')
        number_jumble.remove('R')
        number_jumble.remove('O')
        number_digits_array[0] += 1
    while 'W' in number_jumble:
        number_jumble.remove('T')
        number_jumble.remove('W')
        number_jumble.remove('O')
        number_digits_array[2] += 1
    while 'U' in number_jumble:
        number_jumble.remove('F')
        number_jumble.remove('O')
        number_jumble.remove('U')
        number_jumble.remove('R')
        number_digits_array[4] += 1
    while 'R' in number_jumble:
        number_jumble.remove('T')
        number_jumble.remove('H')
        number_jumble.remove('R')
        number_jumble.remove('E')
        number_jumble.remove('E')
        number_digits_array[3] += 1
    while 'O' in number_jumble:
        number_jumble.remove('O')
        number_jumble.remove('N')
        number_jumble.remove('E')
        number_digits_array[1] += 1
    while 'F' in number_jumble:
        number_jumble.remove('F')
        number_jumble.remove('I')
        number_jumble.remove('V')
        number_jumble.remove('E')
        number_digits_array[5] += 1
    while 'X' in number_jumble:
        number_jumble.remove('S')
        number_jumble.remove('I')
        number_jumble.remove('X')
        number_digits_array[6] += 1
    while 'S' in number_jumble:
        number_jumble.remove('S')
        number_jumble.remove('E')
        number_jumble.remove('V')
        number_jumble.remove('E')
        number_jumble.remove('N')
        number_digits_array[7] += 1
    while 'G' in number_jumble:
        number_jumble.remove('E')
        number_jumble.remove('I')
        number_jumble.remove('G')
        number_jumble.remove('H')
        number_jumble.remove('T')
        number_digits_array[8] += 1
    while 'I' in number_jumble:
        number_jumble.remove('N')
        number_jumble.remove('I')
        number_jumble.remove('N')
        number_jumble.remove('E')
        number_digits_array[9] += 1

    index = 0
    phone_number_string = ""
    while index < 10:
        if number_digits_array[index] > 0:
            number_digits_array[index] -= 1
            phone_number_string += str(index)
        else:
            index += 1
    return phone_number_string


input_file = "A-large_getting_the_digits.in"

with open(input_file, 'r') as file_object_in:
    lines = file_object_in.readlines()
    testcases = int(lines[0].strip())
    case_number = 0
    output_file = "getting_the_digits_large_output.txt"

    while case_number < testcases:
        case_number += 1
        number_jumble = lines[case_number].strip()
        with open(output_file, 'a') as file_object_out:
            file_object_out.write("Case #" + str(case_number) + ": " + get_digits(number_jumble) + "\n")