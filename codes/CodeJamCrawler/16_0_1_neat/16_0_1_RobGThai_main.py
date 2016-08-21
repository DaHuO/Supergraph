
def algo(n, i):
    return n * i

def clean_line(line):
    return line.replace('\r', '').replace('\n', '')

def begin(file):
    with open(file) as input:
        input_size = long(input.readline())
        for no, line in enumerate(input):
            start_counting(no, long(clean_line(line)))

def start_counting(case, start_number):
    req = '0123456789'
    max_iter = 20000
    attempt = 0
    last_number = None
    insomnia = 'INSOMNIA'

    while req and attempt < max_iter:
        attempt += 1
        digits = algo(attempt, start_number)

        for digit in str(digits):
            # print digit, (digit in req)
            if digit in req:
                req = req.replace(digit, '')

            if not req:
                last_number = digits
                break

    print_case(case_number(case), last_number if last_number else insomnia)


def case_number(pos):
    return pos + 1

def print_case(case_no, answer):
    print 'Case #{case_no}: {answer}' \
        .format(
            case_no = case_no,
            answer = answer
        )

if __name__ == '__main__':
    begin('sheep/A-large.in')
