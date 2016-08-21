def recurse_trot(n, i, n_seen):
    print(n_seen)
    if n == 0:
        return 'INSOMNIA'
    else:
        for digit in str(i * n):
            n_seen.add(digit)
        if len(n_seen) == 10:
            return n * i
        else:
            i += 1
            return recurse_trot(n, i, n_seen)

def get_output(i):
    return recurse_trot(i, 1, set())

with open('A-large.in', 'r') as f:
    _input = [line.strip() for line in f.readlines()]
    num_test_cases = _input[0]
    _input = _input[1:]
    with open('output.txt', 'w') as fo:
        for i, line in enumerate(_input):
            out = 'Case #' + str(i + 1) + ': ' + str(get_output(int(line))) + '\n'
            print(line)
            print(out)
            fo.write(out)
