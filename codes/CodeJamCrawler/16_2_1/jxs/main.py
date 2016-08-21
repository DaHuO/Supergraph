#! /usr/bin/env python3

T = int(input())

for case_nr in range(T):
    S = list(input())

    digits = []

    while ('Z' in S):
        S.remove('Z')
        S.remove('E')
        S.remove('R')
        S.remove('O')
        digits.append(0)

    while ('W' in S):
        S.remove('T')
        S.remove('W')
        S.remove('O')
        digits.append(2)

    while ('U' in S):
        S.remove('F')
        S.remove('O')
        S.remove('U')
        S.remove('R')
        digits.append(4)

    while ('F' in S):  # after four
        S.remove('F')
        S.remove('I')
        S.remove('V')
        S.remove('E')
        digits.append(5)

    while ('X' in S):
        S.remove('S')
        S.remove('I')
        S.remove('X')
        digits.append(6)

    while ('V' in S):  # after five
        S.remove('S')
        S.remove('E')
        S.remove('V')
        S.remove('E')
        S.remove('N')
        digits.append(7)

    while ('G' in S): 
        S.remove('E')
        S.remove('I')
        S.remove('G')
        S.remove('H')
        S.remove('T')
        digits.append(8)

    while ('H' in S):  # after eight
        S.remove('T')
        S.remove('H')
        S.remove('R')
        S.remove('E')
        S.remove('E')
        digits.append(3)

    while ('O' in S): ##
        S.remove('O')
        S.remove('N')
        S.remove('E')
        digits.append(1)

    while (S): ##
        S.remove('N')
        S.remove('I')
        S.remove('N')
        S.remove('E')
        digits.append(9)

    digits = sorted(digits)
    number = [ str(i) for i in digits ]
    print("Case #{}: {}".format(case_nr+1, "".join(number)))

