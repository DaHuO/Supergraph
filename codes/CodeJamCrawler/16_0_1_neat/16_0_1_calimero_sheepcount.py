

def track_digits(x, history):
    while x > 0:
        history |= 1 << (x % 10)
        x //= 10
    return history


def count(x):

    if x == 0: return 'INSOMNIA'

    history = 0
    i = 1
    while True:
        history = track_digits(x * i, history)
        if history == 0x3ff:
            return i * x

        i += 1


def test_cases(path):
    for i, l in enumerate(open(path)):
        if i > 0:
            yield(int(i), int(l))

if __name__ == '__main__':
    with open('sheep/large.out', 'w') as o:
        for case in test_cases('sheep/A-large.in'):
            case_str = 'Case #{}: {}\n'.format(case[0], count(case[1]))
            o.write(case_str)
