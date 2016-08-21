#!/usr/bin/env python
import sys
import string  

def solve(inputw):


    inputword = list(inputw)


    lenth = len(inputword)
    new_word = inputword[0]


    for n in xrange(1,lenth):


        if inputword[n] >= new_word[0]:

            new_word = inputword[n] + new_word
        else:
            new_word = new_word + inputword[n]
    return new_word




def process(f):
    case_num = int(f.readline())
    for t in xrange(case_num):
        inputword = f.readline().strip()
        #print inputword
        s = solve(inputword)

        

        print 'Case #%d: %s' % (t+1, s)


def main():
    with open(sys.argv[1]) as f:
        

        process(f)

if __name__ == '__main__':
    main()
