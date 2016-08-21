# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:50:14 2016

@author: James
"""

import sys
import os

def make_answer(string):
    char_counts = {}
    chars_left = len(string)
    phone_number = []
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    i = 0
    chars = ("Z", "W", "U", "X", "G", "O", "H", "F", "S", "I")
    matching_digits = ("0", "2", "4", "6", "8", "1", "3", "5", "7", "9")
    numbers = ("ZERO", "TWO", "FOUR", "SIX", "EIGHT", 
               "ONE", "THREE", "FIVE", "SEVEN", "NINE")
    while chars_left > 0 and i < 10:
        current_char = chars[i]
        if char_counts.get(current_char, 0) > 0:
            for char in numbers[i]:
                char_counts[char] -= 1
            phone_number.append(matching_digits[i])
        else:
            i += 1
    phone_number.sort()
    return ''.join(phone_number)
    
def rdln(txtin):
    return txtin.readline().strip()

def file_io():
    file_names = 'A'
    with open(''.join([file_names, '.in'])) as txtin, \
         open(''.join([file_names, '.out']), 'w') as txtout:
        case_count = int(rdln(txtin))
        for i in range(case_count):
            
            jumbled_number = rdln(txtin)
            answer = make_answer(jumbled_number)
                                
            str_out = str(answer)
            txtout.write(''.join(['Case #', str(i + 1), ': ']))
            txtout.write(str_out)
            txtout.write('\n')
    osCommandString = ''.join(['notepad.exe ', file_names, '.out'])
    os.system(osCommandString)

def main():
    """Main"""
    file_io()

if __name__ == '__main__':
    sys.exit(main())
