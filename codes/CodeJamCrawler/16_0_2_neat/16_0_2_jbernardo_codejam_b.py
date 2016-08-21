import re


def gen_stack(data):
    return [x == '+' for x in data]


def read_file_simple(name, fn=str):
    with open(name) as file:
        lines = iter(file)
        ncases = int(next(lines))

        return [fn(next(lines).strip()) for _ in range(ncases)]


def solve(input_file, func, read_func, stdout=False):
    input_data = read_func(input_file)

    text = '\n'.join(
        'Case #{}: {}'.format(i, func(data))
        for i, data in enumerate(input_data, 1)
    )

    if stdout:
        print(text)
    else:
        with open(input_file + '.out', 'w') as file:
            print(text, file=file)


def flip(stack, amount):
    stack[:amount] = [not x for x in stack[:amount]][::-1]
    return stack


def func_b(stack):
    top = stack[0]
    stack = re.sub('[%s]+' % top, top, stack)
    return (top == '-') + 2 * len(re.findall('[+]+[-]+', stack))


if __name__ == '__main__':
    solve('tests/B-large.in', func_b, read_file_simple, False)
