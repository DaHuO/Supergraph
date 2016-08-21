#!/usr/bin/python

def find_last_word(start_word):
    '''
    Using rules of the game, return the last of an alphabetically sorted list
    of all of the possible last words that could have been produced.
    :param start_word: input word
    :return: last_word: string that is alphabetically last
    '''
    last_word = start_word[0]
    for index in range(1, start_word.__len__()):
        if start_word[index] < last_word[0]:
            last_word += start_word[index]
        else:
            last_word = start_word[index] + last_word
    return last_word


input_file = "Last_Word_A-large.in"

with open(input_file, 'r') as file_object_in:
    lines = file_object_in.readlines()
    testcases = int(lines[0].strip())
    case_number = 0
    output_file = "last_word_large_output.txt"

    while case_number < testcases:
        case_number += 1
        start_word = lines[case_number].strip()
        with open(output_file, 'a') as file_object_out:
            file_object_out.write("Case #" + str(case_number) + ": " + find_last_word(start_word) + "\n")