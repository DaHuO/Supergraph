import sys


def read_input(in_file):
    out_file = in_file.split('.')[0] + '.out'
    with open(in_file, 'r') as i, open(out_file, 'w') as o:
        number_of_cases = int(i.readline())
        for index in range(1, number_of_cases + 1):
            line = i.readline()
            output = calculate_insomnia(int(line))
            print(output)
            o.write('Case #{0}: {1}\n'.format(index, str(output)))


def calculate_insomnia(n):
    seen_digits = set()
    seen_numbers = []

    is_insomnia = False

    i = 1
    while not is_insomnia and len(seen_digits) < 10:
        current_number = i * n
        seen_digits.update(list(str(current_number)))
        if current_number in seen_numbers:
            is_insomnia = True
        seen_numbers.append(current_number)
        i += 1
    return 'INSOMNIA' if is_insomnia else current_number

if __name__ == '__main__':
    read_input(sys.argv[1])
