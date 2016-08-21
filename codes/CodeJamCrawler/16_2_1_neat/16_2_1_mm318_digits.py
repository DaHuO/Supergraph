import os, sys, inspect

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if not(cmd_folder in sys.path):
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], 'libs')))
if not(cmd_subfolder in sys.path):
    sys.path.insert(0, cmd_subfolder)


import errno
import re
from collections import defaultdict
from itertools import izip_longest
import subprocess


def Tree():
    return defaultdict(Tree)


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main(args):
    in_file_path = args[1]
    in_file = open(in_file_path, 'rb')
    
    T = int(in_file.readline())
    for i in range(T):
        S = in_file.readline().strip()

        letter_counts = defaultdict(int)
        for letter in alphabet:
            letter_counts[letter] = S.count(letter)

        digits = ''
        if(letter_counts['Z'] > 0):
            count = letter_counts['Z']
            digits += '0' * count
            letter_counts['Z'] -= count
            letter_counts['E'] -= count
            letter_counts['R'] -= count
            letter_counts['O'] -= count
        if(letter_counts['W'] > 0):
            count = letter_counts['W']
            digits += '2' * count
            letter_counts['T'] -= count
            letter_counts['W'] -= count
            letter_counts['O'] -= count
        if(letter_counts['X'] > 0):
            count = letter_counts['X']
            digits += '6' * count
            letter_counts['S'] -= count
            letter_counts['I'] -= count
            letter_counts['X'] -= count
        if(letter_counts['U'] > 0):
            count = letter_counts['U']
            digits += '4' * count
            letter_counts['F'] -= count
            letter_counts['O'] -= count
            letter_counts['U'] -= count
            letter_counts['R'] -= count
        if(letter_counts['O'] > 0):
            count = letter_counts['O']
            digits += '1' * count
            letter_counts['O'] -= count
            letter_counts['N'] -= count
            letter_counts['E'] -= count
        if(letter_counts['S'] > 0):
            count = letter_counts['S']
            digits += '7' * count
            letter_counts['S'] -= count
            letter_counts['E'] -= count
            letter_counts['V'] -= count
            letter_counts['E'] -= count
            letter_counts['N'] -= count
        if(letter_counts['G'] > 0):
            count = letter_counts['G']
            digits += '8' * count
            letter_counts['E'] -= count
            letter_counts['I'] -= count
            letter_counts['G'] -= count
            letter_counts['H'] -= count
            letter_counts['T'] -= count
        if(letter_counts['T'] > 0):
            count = letter_counts['T']
            digits += '3' * count
            letter_counts['T'] -= count
            letter_counts['H'] -= count
            letter_counts['R'] -= count
            letter_counts['E'] -= count
            letter_counts['E'] -= count
        if(letter_counts['V'] > 0):
            count = letter_counts['V']
            digits += '5' * count
            letter_counts['F'] -= count
            letter_counts['I'] -= count
            letter_counts['V'] -= count
            letter_counts['E'] -= count
        if(letter_counts['I'] > 0):
            count = letter_counts['I']
            digits += '9' * count
            letter_counts['N'] -= count
            letter_counts['I'] -= count
            letter_counts['N'] -= count
            letter_counts['E'] -= count

        digits = sorted(digits)

        print 'Case #%d: %s' % (i+1, ''.join(digits))

    return 0


if(__name__ == "__main__"):
    ret = main(sys.argv)
    sys.exit(ret)

