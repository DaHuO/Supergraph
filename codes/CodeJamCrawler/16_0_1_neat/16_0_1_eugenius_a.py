import sys
from funcy import count

STDIN = sys.stdin
num_cases = int(STDIN.readline())

def get_digits_from_number(num):
    return set(str(num))

def generate_number_sequence(n):
    current_number = n
    i = 1
    digits_set = set()

    if n == 0:
        return 'INSOMNIA'

    while True:
        current_number = n * i

        i += 1
        digits = get_digits_from_number(current_number)
        digits_set = digits_set | digits

        if len(digits_set) == 10:
            return current_number

def parse_case():
    num = int(STDIN.readline())
    return generate_number_sequence(num)

for case in range(num_cases):
    output = parse_case()
    print 'Case #{}: {}'.format(case+1, output)

