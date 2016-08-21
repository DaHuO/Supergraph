"""
Created on 08/05/2016

@author: Dos

Problem A. Senate Evacuation
https://code.google.com/codejam/contest/


***Sample***

Input
4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1

Output
Case #1: AB BA
Case #2: AA BC C BA
Case #3: C C AB
Case #4: BA BB CA

"""

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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
    P = kwargs['P']

    exit = ""

    if sum(P) % 2 == 1:
        m1 = max(P)
        i1 = P.index(m1)
        P[i1] -= 1
        exit += A[i1]
        exit += " "

    while sum(P) > 0:

        m1 = max(P)
        i1 = P.index(m1)
        P[i1] -= 1
        exit += A[i1]

        m2 = max(P)
        i2 = P.index(m2)
        P[i2] -= 1
        exit += A[i2]
        exit += " "

    return "Case #{}: {}\n".format(case, exit)


# INPUT_FILE_NAME = "A-sample.in"
# INPUT_FILE_NAME = "A-small-attempt2.in"
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
        N = read_int(input_file)
        P = read_ints(input_file)
        args = {'N': N, 'P': P, }

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
