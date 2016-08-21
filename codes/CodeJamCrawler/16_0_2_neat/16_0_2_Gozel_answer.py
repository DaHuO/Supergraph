import os
script_path = os.path.dirname(__file__)


def remove_happy_faces_at_bottom(str):
    last_char = str[-1:]
    while last_char == '+':
        str = str[:-1]
        last_char = str[-1:]
    return str


def count_blank_groups(str):
    i, sequence, result = 0, 0, 0
    for s in str:
        if s == '-':
            sequence += 1
        else:
            result += 1 if sequence > 0 else False
            sequence = 0
        i += 1
    result += 1 if sequence > 0 else False
    if result == 1 and str[0] == '-' and str.count('+') > 0:
        result = 0
    return result


def take_first_blanks(str):
    result = ''
    sequence = 0
    for s in str:
        if s == '-':
            sequence += 1
        if s == '+' and sequence > 0:
            return result
        result += s
    return result


def flip(str):
    result = ''
    # reverse the string
    str = str[::-1]
    if len(str) == 2:
        return str
    # replace each + to - and each - to + in string
    for s in str:
        result += '+' if s == '-' else '-'
    return result


def is_everyone_happy(str):
    string_length = len(str)
    happy_faces_length = str.count('+')
    return True if string_length == happy_faces_length else False


def shortest_path_to_happiness(str):
    flip_counter = 0
    while is_everyone_happy(str) == False:
        # make everyone happy
        str = remove_happy_faces_at_bottom(str)
        c = count_blank_groups(str)
        if c == 1:
            flip_counter += 1 if len(str) == str.count('-') else 2
            break
        if str[0] == str[-1:]:
            str = flip(str)
            flip_counter += 1
        else:
            if str[0] != str[-1:]:
                str_first_blanks = take_first_blanks(str)
                if str_first_blanks[0] == str_first_blanks[-1:]:
                    str_first_blanks = flip(str_first_blanks)
                    flip_counter += 1
                    str = str_first_blanks + str[len(str_first_blanks):]
                else:
                    flip_counter += 2
                    str = '+' + str[len(str_first_blanks):]
    return flip_counter

# read input file line by line
with open(os.path.join(script_path, 'B-large.in')) as f:
    input = [x.strip('\n') for x in f.readlines()]

# create desired output
output = ''
case_no = 1
for l in range(1, len(input), 1):
    input[l] = input[l][0:101]
    result = str(shortest_path_to_happiness(input[l]))
    output += 'Case #' + str(case_no) + ':' + ' ' + result + '\n'
    case_no += 1
    if case_no == 101:
        break

f = open(os.path.join(script_path, 'output.txt'), 'w')
f.write(output)
f.close()
