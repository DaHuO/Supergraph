import sys

def read_file_lines():
    if len(sys.argv) < 2:
        print('First argument should be the dataset file')
        exit(1)

    with open(sys.argv[1]) as f:
        file_lines = [line.strip() for line in f.readlines()]
    return file_lines


def get_inputs():
    inputs = [int(i) for i in read_file_lines()]

    assert(inputs[0] == len(inputs[1:]))
    return inputs[1:]


def split_digits(n):
    return set(int(i) for i in str(n))


if __name__ == '__main__':
    all_digits = set(range(10))

    for index, v in enumerate(get_inputs()):
        if v == 0:
            print('Case #%d: INSOMNIA' % (index + 1))
            continue

        n = 1
        seen_digits = split_digits(v * n)

        for n in range(10000):
            n += 1
            seen_digits |= split_digits(v * n)
            if seen_digits == all_digits:
                print('Case #%d: %d' % (index + 1, v * n))
                break
