"""
    Oh YUSSS
"""

def get_number_flips(input_string):
    """
        Return minimal number of flips for string
    """
    n = 0
    if input_string[0] == '+':
        while '-' in input_string:
            input_string = flip_start_pluses(input_string)
            input_string = flip_lowest_minus(input_string)
            n+=2
        return n
    else:
        input_string = flip_lowest_minus(input_string)
        n += 1
        while '-' in input_string:
            input_string = flip_start_pluses(input_string)
            input_string = flip_lowest_minus(input_string)
            n+=2
        return n
    return n


def flip_until(input,i):
    return ''.join([flip_char(char) for char in reversed(input[:i])])+input[i:]

def flip_lowest_minus(input):
    if '-' in input:
        ind = input.rfind('-')+1
        return flip_until(input, ind)


def flip_start_pluses(input):
    if input[0] == '+':
        i = 1
        while i < len(input):
            if input[i] == '-':
                return flip_until(input, i)
            i += 1

    else:
        return input


def flip_char(input):
    if input == '-':
        return '+'
    else:
        return '-'

with open('B-large.in') as ifile:
    with open('output.out', 'w') as ofile:
        ifile.readline()
        i = 1
        for line in ifile:
            ret = 'Case #{}: {}\n'.format(i, get_number_flips(line))
            ofile.write(ret)
            i += 1
