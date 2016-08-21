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


def main(args):
    in_file_path = args[1]
    in_file = open(in_file_path, 'rb')
    
    T = int(in_file.readline())
    for i in range(T):
        S = in_file.readline().strip()

        last_word = S[0]
        for letter in S[1:]:
            if(letter >= last_word[0]):
                last_word = letter + last_word
            else:
                last_word += letter

        print 'Case #%d: %s' % (i+1, last_word)

    return 0


if(__name__ == "__main__"):
    ret = main(sys.argv)
    sys.exit(ret)

