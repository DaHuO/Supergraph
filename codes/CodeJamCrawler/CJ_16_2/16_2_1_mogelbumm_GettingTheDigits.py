'''
Created on 11.04.2015

@author: uscheller
'''
import sys
import math


NUMBER_MAP = (
           ("4" , "FOUR"),
           ("5" , "FIVE"),
           ("6" , "SIX"),
           ("7" , "SEVEN"),
           ("8" , "EIGHT"),
           ("9" , "NINE"),
           ("0" , "ZERO"),
           ("3" , "THREE"),
           ("1" , "ONE"),
           ("2" , "TWO"),
           )

def remove_chars(S, chars):
    for c in chars:
        S = S[: S.index(c)] + S[S.index(c) + 1 :]
    return S

def all_chars_in(chars, S):
    s_clone = S[:]
    for c in chars:
        if c in s_clone:
            s_clone = s_clone[: s_clone.index(c)] + s_clone[s_clone.index(c) + 1 :]
        else:
            return False
    return True

def next_number_in(S):
    for digit, chars in NUMBER_MAP:
        if all_chars_in(chars, S):
            return digit, remove_chars(S, chars)
        

def solve(S):
    s = ""
    while S != "":
        number, S = next_number_in(S)
        s += number
    return "".join(sorted(s))

def go_through(data):
    data = data[1:]
    s = ""
    case = 1
    while len(data) > 0:
        S = data[0].replace("\n", "")
        data = data[1:]
        s += "Case #%d: %s\n" % (case, solve(S))
        case += 1
    return s[:-1] # remove newline

if __name__ == '__main__':
    print go_through(open(sys.argv[1]).readlines())