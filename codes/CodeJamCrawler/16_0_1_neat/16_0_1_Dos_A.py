"""
Created on 02/05/2015

@author: Dos

Problem A.
https://code.google.com/codejam/contest/


***Sample***

Input
WRITE_INTPUT_HERE

Output
WRITE_OUTPUT_HERE

"""


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_words(f, d=' '):
    return read_word(f).split(d)


def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]


def read_decimals(f, d=' '):
    return [float(x) for x in read_words(f, d)]


def solve(case, **kwargs):
    # get problem data
    N = kwargs['N']

    counter = {
        '0': True,
        '1': True,
        '2': True,
        '3': True,
        '4': True,
        '5': True,
        '6': True,
        '7': True,
        '8': True,
        '9': True,
    }

    if not N:
        curr = "INSOMNIA"
    else:
        i = 1
        curr = N
        while counter:
            # print curr, counter
            for c in str(curr):
                if c in counter:
                    del counter[c]
            if counter:
                curr = N * i
                i += 1

    return "Case #{}: {}\n".format(case, curr)


# INPUT_FILE_NAME = "A-sample.in"
# INPUT_FILE_NAME = "A-small-attempt0.in"
INPUT_FILE_NAME = "A-large.in"

# OUTPUT_FILE_NAME = "A-sample.out"
# OUTPUT_FILE_NAME = "A-small-attempt0.out"
OUTPUT_FILE_NAME = "A-large.out"

if __name__ == '__main__':

    # create I/O files
    input_file = open(INPUT_FILE_NAME, 'r')
    output_file = open(OUTPUT_FILE_NAME, "w")

    # read file size
    T = read_int(input_file)
    print("\nThere are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in xrange(1, T+1):
        # read input args
        n = read_int(input_file)
        args = {'N': n, }

        # print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
