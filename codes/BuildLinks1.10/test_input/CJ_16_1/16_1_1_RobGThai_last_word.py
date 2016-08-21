import random, string

def case_number(pos):
    return pos + 1

def print_case(case_no, answer):
    print 'Case #{case_no}: {answer}' \
        .format(
            case_no = case_no,
            answer = answer
        )

def clean_line(line):
    return line.replace('\r', '').replace('\n', '')

def solve(line):
    result = line[0]
    for c in line[1:]:
        if c >= result[0]:
            result = c + result
        else:
            result += c

    return result

def begin(file):

    with open(file) as input:
        input_size = long(input.readline())
        for no, line in enumerate(input):
            print_case(no+1, solve(clean_line(line)))

if __name__ == '__main__':
    begin('round_1a/last_word/A-large.in')
