#!/user/bin/env python
"""Google Code Jam 2016: Problem A. Getting The Digits"""

from builtins import input

def main():
    T = int(input())
    if T < 1 or T > 100:
        raise RuntimeError("T is not within the valid range")
    for i in range(T):
        S = input()
        r = GettingTheDigits(S)
        print("Case #" + str(i + 1) + ": " + r)

def GettingTheDigits(S):
    ZERO = S.count('Z')
    S = S.replace('Z', '', ZERO).replace('E', '', ZERO).replace('R', '',
            ZERO).replace('O', '', ZERO)
    TWO = S.count('W')
    S = S.replace('T', '', TWO).replace('W', '', TWO).replace('O', '', TWO)
    SIX = S.count('X')
    S = S.replace('S', '', SIX).replace('I', '', SIX).replace('X', '', SIX)
    SEVEN = S.count('S')
    S = S.replace('S', '', SEVEN).replace('E', '', SEVEN * 2).replace('V', '',
            SEVEN).replace('N', '', SEVEN)
    FOUR = S.count('U')
    S = S.replace('F', '', FOUR).replace('O', '', FOUR).replace('U', '',
            FOUR).replace('R', '', FOUR)
    FIVE = S.count('V')
    S = S.replace('F', '', FIVE).replace('I', '', FIVE).replace('V', '',
            FIVE).replace('E', '', FIVE)
    EIGHT = S.count('G')
    S = S.replace('E', '', EIGHT).replace('I', '', EIGHT).replace('G', '',
            EIGHT).replace('H', '', EIGHT).replace('T', '', EIGHT)
    THREE = S.count('H')
    S = S.replace('T', '', THREE).replace('H', '', THREE).replace('R', '',
            THREE).replace('E', '', THREE*2)
    ONE = S.count('O')
    S = S.replace('O', '', ONE).replace('N', '', ONE).replace('E', '', ONE)
    NINE = S.count('I')

    r = '0' * ZERO + '1' * ONE + '2' * TWO + '3' * THREE + '4' * FOUR 
    r += '5' * FIVE + '6' * SIX + '7' * SEVEN + '8' * EIGHT + '9' * NINE
    return r


if __name__=="__main__":
    main()
