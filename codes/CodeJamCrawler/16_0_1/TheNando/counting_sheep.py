import sys


def chain(*funcs):
    def run_funcs(args):
        index = len(funcs)
        while index:
            index -= 1
            args = funcs[index](args)
        return args
    return run_funcs


def read_input(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def write_results(results, filename):
    with open(filename, 'w') as f:
        f.writelines(results)


def count_sheep(n):
    if not n:
        return 'INSOMNIA'

    digits = set('0123456789')
    factor = 0

    while len(digits):
        factor += 1
        digits = digits.difference(str(n * factor))

    return n * factor


# get script name
name = sys.argv[0].split('/').pop().split('.')[0]

# read trials from script input file
trials = read_input('in.{}.txt'.format(name))

# Don't need to know how many trials to run
trials.pop(0)

# run trials and collect results
data = [count_sheep(int(trial)) for trial in trials]

# create output strings from results
output = ['Case #{}: {}\n'.format(i + 1, result) for i, result in enumerate(data)]

# write output
write_results(output, 'out.{}.txt'.format(name))
