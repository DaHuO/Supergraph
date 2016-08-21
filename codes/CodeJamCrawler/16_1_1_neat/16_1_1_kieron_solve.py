#!/usr/bin/python

import sys

#debug_on = True
debug_on = False

if (len(sys.argv) == 2):
    input_file = open(sys.argv[1], 'r')

else:
    print "Input file not specified"
    sys.exit(1)

num_cases = int(input_file.readline().strip())

def pdebug(line):
    if debug_on:
        print line

for i in (range(1, num_cases + 1)):

    # read the data
    word = input_file.readline().strip()
    pdebug(word)

    word_out = []
    word_out.append(word[0])

    for char in word[1:]:
        pdebug("comparing %s to %s" % (char, word_out[0]))
        if char >= word_out[0]:
            pdebug("placing %s at beginning" % char)
            word_out.insert(0, char)
        else:
            pdebug("placing %s at end" % char)
            word_out.append(char)


    # print the summary line for this case
    print "Case #%s: %s" % (i, ''.join(word_out))
