import numpy as np
from collections import Counter

c_0 = sorted('ZERO')    # Z
c_1 = sorted('ONE')     # O, if no TWO and FOUR
c_2 = sorted('TWO')     # W
c_3 = sorted('THREE')   # R, if no ZERO and FOUR
c_4 = sorted('FOUR')    # U
c_5 = sorted('FIVE')    # F, if no FOUR
c_6 = sorted('SIX')     # X
c_7 = sorted('SEVEN')   # S, if no SIX
c_8 = sorted('EIGHT')   # G
c_9 = sorted('NINE')    # N, if no ONE and SEVEN

def solve(S):
    S = sorted(S)
    counter = Counter(S)
    answer = []
    while counter['Z'] > 0: # find ZERO
        for c in c_0:
            counter[c] -= 1
        answer.append('0')
    while counter['W'] > 0: # find TWO
        for c in c_2:
            counter[c] -= 1
        answer.append('2')
    while counter['X'] > 0: # find SIX
        for c in c_6:
            counter[c] -= 1
        answer.append('6')
    while counter['U'] > 0: # find FOUR
        for c in c_4:
            counter[c] -= 1
        answer.append('4')
    while counter['G'] > 0: # find EIGHT
        for c in c_8:
            counter[c] -= 1
        answer.append('8')
    while counter['S'] > 0: # find SEVEN
        for c in c_7:
            counter[c] -= 1
        answer.append('7')
    while counter['F'] > 0: # find FIVE
        for c in c_5:
            counter[c] -= 1
        answer.append('5')
    while counter['R'] > 0: # find THREE
        for c in c_3:
            counter[c] -= 1
        answer.append('3')
    while counter['O'] > 0: # find ONE
        for c in c_1:
            counter[c] -= 1
        answer.append('1')
    while counter['N'] > 0: # find NINE
        for c in c_9:
            counter[c] -= 1
        answer.append('9')
    return ''.join(sorted(answer))
def main():
    testcases = input()
    for case_num in xrange(1, testcases+1):
        S = raw_input()
        print("Case #%i: %s" % (case_num, solve(S)))

def test():
    single_case = raw_input()
    print("Case #1: %s" % (solve(single_case)))


if __name__=='__main__':
    main()
    #test()

