#!/usr/bin/python

import sys


def try_to_sleep(n):
    digits = set([str(i) for i in range(10)])
    last_number_str = None
    number = n
    while True:
        number_str = str(number)
        number += n
        digits.difference_update(set([c for c in number_str]))
        if last_number_str and last_number_str == number_str:
            return "INSOMNIA"
        elif digits:
            last_number_str = number_str
        else:
            return number_str

def run_test(n_list, out_file):
    lines = [
        "Case #{0}: {1}\n".format(i + 1, try_to_sleep(n))
        for i, n in enumerate(n_list)
    ]

    with open(out_file, 'w+') as f:
        f.writelines(lines)

def parse_input_file(in_file):
    with open(in_file, 'r') as f:
        read_data = f.read()

    code_input = read_data.split('\n')
    t = int(code_input.pop(0))
    return [int(i) for i in code_input[0:t]]

def get_files():
    in_file = sys.argv[1]
    base_file_name = in_file.split('.')[0]
    out_file = "{0}.out".format(base_file_name)
    return in_file, out_file

def main():
    if len(sys.argv) < 2:
        print "Usage: python {0} <Input File>".format(sys.argv[0])
    else:
        in_file, out_file = get_files()
        code_input = parse_input_file(in_file)
        run_test(code_input, out_file)
        sys.exit(0)

    sys.exit(1)

if __name__ == '__main__':
    main()
