#!/usr/bin/env python3

import sys

def last_word(s):
    word = s[0]
    for c in s[1:]:
        if c < word[0]:
            word += c
        else:
            word = c+word
    return word

def main():
    if len(sys.argv) < 2:
        print("Usage: last_word.py <file>")
        exit()
    in_file = sys.argv[1]
    with open(in_file) as f:
        cases = int(f.readline())
        for i, line in enumerate(f):
            s = line.strip() # Strip off the newline
            print("Case #%d: %s" % (i+1, last_word(s)))

##########

if __name__ == '__main__':
    main()
