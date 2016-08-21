import sys


def read_input(in_file):
    out_file = in_file.split('.')[0] + '.out'
    with open(in_file, 'r') as i, open(out_file, 'w') as o:
        number_of_cases = int(i.readline())
        for index in range(1, number_of_cases + 1):
            line = i.readline()
            result = do_algorithm(line.strip())
            output = 'Case #{0}: {1}\n'.format(index, str(result))
            print(output)
            o.write(output)


def flip_top(input):
    tmp = input[::-1]
    return flip_string_signs(tmp)


def flip_string_signs(tmp):
    tmp = tmp.replace('+', 'x')
    tmp = tmp.replace('-', '+')
    tmp = tmp.replace('x', '-')
    return tmp


def do_algorithm(input):
    input = input[::-1]

    number_of_flips = 0
    while not is_happy_side_up(input):
        if input[0] == '-':
            if input[-1] == '+':
                for i in range(1, len(input)):
                    if input[i:] == '+' * (len(input) - i):
                        input = input[0:i] + '-' * (len(input) - i)
                        number_of_flips += 1
                        break
            input = flip_top(input)
            number_of_flips += 1
        input = input[1:]

    return number_of_flips


def is_happy_side_up(input):
    return input == (len(input) * '+')


if __name__ == '__main__':
    read_input(sys.argv[1])
