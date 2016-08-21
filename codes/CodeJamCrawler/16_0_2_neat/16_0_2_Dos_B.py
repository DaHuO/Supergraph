"""
Created on 02/05/2015

@author: Dos

Problem B. Revenge of the Pancakes
https://code.google.com/codejam/contest/6254486/dashboard#s=p1


***Sample***

Input
5
-
-+
+-
+++
--+-

Output
Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3


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
    s = kwargs['stack']

    maneuvers = 0
    if s[-1] == '-':
        s = s[::-1]
        maneuvers += 1

    curr = s[0]
    for i in s[1:]:
        if i != curr:
            maneuvers += 1
            curr = i

    return "Case #{}: {}\n".format(case, maneuvers)


# INPUT_FILE_NAME = "B-sample.in"
# INPUT_FILE_NAME = "B-small-attempt0.in"
INPUT_FILE_NAME = "B-large.in"

# OUTPUT_FILE_NAME = "B-sample.out"
# OUTPUT_FILE_NAME = "B-small-attempt0.out"
OUTPUT_FILE_NAME = "B-large.out"

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
        stack = read_word(input_file)
        args = {'stack': stack, }

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
