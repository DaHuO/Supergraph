from itertools import groupby

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


class Flipinator():

    def group(self, pancakes):
        return groupby(pancakes)

    def flipping(self, case, pancakes):
        g = self.group(pancakes)
        pancakes = [x for x, _ in g]

        flips = len(pancakes)
        if pancakes[-1] == '+': flips -= 1
        print_case(case_number(case), flips)

def start_flipping(no, pancakes):
    Flipinator().flipping(no, pancakes)

def begin(file):
    with open(file) as input:
        input_size = long(input.readline())
        for no, line in enumerate(input):
            start_flipping(no, clean_line(line))

if __name__ == '__main__':
    begin('pancake/B-large.in')
