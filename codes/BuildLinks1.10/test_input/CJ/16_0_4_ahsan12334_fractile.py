# Google Code Jam 2016
# Qualification Round
# Fractiles Problem

from itertools import product

if __name__ == "__main__":
    input_file = open('D-small-attempt0.in', 'r')
    test_cases = input_file.read().split('\n')[1:]
    test_cases = test_cases[:len(test_cases)-1]
    input_file.close()

    output_file = open('output.txt', 'w')

    case_number = 1
    for t in test_cases:
        K, C, S = [int(x) for x in t.split()]

        # If S == K then the solution is trivial
        # If original pattern starts with G
        # Then opening the network C times gives us
        # A sequence such that there is at least one G in the first K tiles
        # If the original pattern stars with L
        # Then opening the network C times
        # Gives us a sequence such that the first K elements contain the original sequence
        # So if G exists in the original pattern it will surely exist in the first K tiles
        # So opening the first K tiles will show us if there was gold in the original
        output_file.write('Case #{0}:'.format(case_number))
        if S < K:
            output_file.write(' IMPOSSIBLE')
        else:
            for n in range(1, K + 1):
                output_file.write(' {0}'.format(n))
        output_file.write('\n')
        case_number += 1
    output_file.close()