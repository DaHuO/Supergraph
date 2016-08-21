import sys
import time

number_map = {
    "ZERO":  0, # Z
    "ONE":   1,
    "TWO":   2, # W
    "THREE": 3,
    "FOUR":  4, # U
    "FIVE":  5, # F,V
    "SIX":   6, # X
    "SEVEN": 7, # S,V
    "EIGHT": 8, # G
    "NINE":  9,
}

trimmed_number_map = {
    "ONE":   1, # O
    "THREE": 3, # H
    "FIVE":  5, # F
    "SEVEN": 7, # V
    "NINE":  9, # N
}

def main(input):
    # First handle the letters we can easily identify
    zeros = input.count('Z')
    input = replace_known(input, zeros, 'ZERO')

    twos = input.count('W')
    input = replace_known(input, twos, 'TWO')

    fours = input.count('U')
    input = replace_known(input, fours, 'FOUR')

    sixes = input.count('X')
    input = replace_known(input, sixes, 'SIX')

    eights = input.count('G')
    input = replace_known(input, eights, 'EIGHT')

    ones = input.count('O')
    input = replace_known(input, ones, 'ONE')

    threes = input.count('H')
    input = replace_known(input, ones, 'THREE')

    fives = input.count('F')
    input = replace_known(input, fives, 'FIVE')

    sevens = input.count('V')
    input = replace_known(input, sevens, 'SEVEN')

    nines = input.count('I')
    input = replace_known(input, nines, 'NINE')

    array = [zeros, ones, twos, threes, fours, fives, sixes, sevens, eights, nines]
    print_string = ''
    for i in xrange(0, 10):
        for j in xrange(0, array[i]):
            print_string += str(i)
    print print_string


def replace_known(input, count, number_string):
    if count: # there is at least one zero
        for i in xrange(0, count):
            for c in number_string:
                input = input.replace(c,'',1) # Replace first occurrence of that letter
    return input

if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(1, T + 1):
        sys.stdout.write("Case #{0}: ".format(i))
        input = raw_input()
        main(input)
