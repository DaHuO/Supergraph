"""
Created on 30/04/2016

@author: Dos

Problem A. Getting the Digits
https://code.google.com/codejam/contest/11254486/dashboard#s=p0


***Sample***

Input
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER

Output
Case #1: 012
Case #2: 2468
Case #3: 114
Case #4: 3

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
    word = kwargs['word']

    string = word
    nums = ''
    tmp = ''

    for c in string:
        if c == 'G':
            nums += '8'
            tmp += 'EIGHT'
        elif c == 'U':
            nums += '4'
            tmp += 'FOUR'
        elif c == 'W':
            nums += '2'
            tmp += 'TWO'
        elif c == 'X':
            nums += '6'
            tmp += 'SIX'
        elif c == 'Z':
            nums += '0'
            tmp += 'ZERO'

    # tmp = sorted(tmp)
    for t in tmp:
        string = string.replace(t, "", 1)

    tmp = ""

    for c in string:
        if c == 'F':
            nums += '5'
            tmp += 'FIVE'
        elif c == 'H':
            nums += '3'
            tmp += 'THREE'
        elif c == 'O':
            nums += '1'
            tmp += 'ONE'
        elif c == 'S':
            nums += '7'
            tmp += 'SEVEN'

    # tmp = sorted(tmp)
    for t in tmp:
        string = string.replace(t, "", 1)

    nums += ('9' * (len(string)/4))

    return "Case #{}: {}\n".format(case, ''.join(sorted(nums)))


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
        w1 = read_word(input_file)
        args = {'word': w1,}

        print("Input #{}:\n{}".format(case, args))
        out = solve(case, **args)
        print(out)
        output_file.write(out)

    # close I/O files
    input_file.close()
    output_file.close()
