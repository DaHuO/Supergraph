# Let's call that obnoxious friend, maybe!

import fileinput

def create_frequency_dict(phone_number_string):
    # Counts up occurrences of letters in the phone number string.
    
    letter_dict = {}
    for letter in phone_number_string:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def process_digit(digit, key_letter, digit_counts, letter_dict, DIGIT_LETTERS):
    # Counts the digit and reduces the dictionary counts accordingly
    
    # No digit, no processing
    if key_letter not in letter_dict or letter_dict[key_letter] == 0:
        return
    
    count = letter_dict[key_letter]
    digit_counts[digit] += count
    for letter in DIGIT_LETTERS[digit]:
        letter_dict[letter] -= count

def get_digits(letter_dict):
    # Given a dictionary of digit letter frequency, determines how many of each
    # digit there are in the scrambled string
    
    #print(letter_dict)
    DIGIT_LETTERS = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',
                     5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'}
    digit_counts = [0]*10;
    #0, 2, 4, 6, 8 have unique characters
    process_digit(0, 'Z', digit_counts, letter_dict, DIGIT_LETTERS)
    process_digit(2, 'W', digit_counts, letter_dict, DIGIT_LETTERS)
    process_digit(4, 'U', digit_counts, letter_dict, DIGIT_LETTERS)
    process_digit(6, 'X', digit_counts, letter_dict, DIGIT_LETTERS)
    process_digit(8, 'G', digit_counts, letter_dict, DIGIT_LETTERS)
    
    # With those removed, 3 and 5 are unique
    process_digit(3, 'H', digit_counts, letter_dict, DIGIT_LETTERS)
    process_digit(5, 'F', digit_counts, letter_dict, DIGIT_LETTERS)
    
    # With those removed, 1 and 7 are unique
    process_digit(1, 'O', digit_counts, letter_dict, DIGIT_LETTERS)
    process_digit(7, 'V', digit_counts, letter_dict, DIGIT_LETTERS)
    
    # Finally, 9
    process_digit(9, 'I', digit_counts, letter_dict, DIGIT_LETTERS)
    
    return digit_counts

def get_phone_number(phone_number_string):
    # Reconstruct a phone number from a scrambled string
    letter_dict = create_frequency_dict(phone_number_string)
    digit_counts = get_digits(letter_dict)
    
    phone_number = ''
    for index in range(len(digit_counts)):
        phone_number += str(index)*digit_counts[index]
    return phone_number

def main():
    firstLine = True
    case = 1
    for line in fileinput.input():
        if firstLine:
            firstLine = False
            continue

        phone_number_string = line.strip()
        print('Case #' + str(case) + ': ', end='')
        print(get_phone_number(phone_number_string))
        
        case += 1


if __name__ == "__main__":
    main()
