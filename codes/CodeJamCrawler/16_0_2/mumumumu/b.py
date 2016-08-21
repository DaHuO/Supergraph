def flip_pancakes(cakes):
    if cakes[0] == '+':
        flips = 0
    else:
        flips = 1

    for i, cake in enumerate(cakes[1:]):
        print(i, cake)
        if cake == '-' and cakes[i + 1 - 1] == '+':
            flips += 2

    return flips


def get_output(i):
    return flip_pancakes(i)

with open('B-large.in', 'r') as f:
    _input = [line.strip() for line in f.readlines()]
    num_test_cases = _input[0]
    _input = _input[1:]
    with open('output.txt', 'w') as fo:
        for i, line in enumerate(_input):
            out = 'Case #' + str(i + 1) + ': ' + str(get_output(line)) + '\n'
            print(line)
            print(out)
            fo.write(out)
