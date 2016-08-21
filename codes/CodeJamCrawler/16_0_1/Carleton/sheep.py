import sys


def parse_file(fname):
    with open(fname, "r") as fh:
        lines = fh.readlines()[1:]

    return [int(l) for l in lines]


def count_sheep(n):

    digits = set()

    if n == 0:
        return "INSOMNIA"

    i=1
    while len(digits) < 10:
        dig_string = "%d" % (n*i)
        next_digs = set(dig_string)
        digits |= next_digs
        i += 1

    return dig_string

def main():
    fname = sys.argv[1]
    outname = sys.argv[2]

    ns = parse_file(fname)

    answers = [count_sheep(n) for n in ns]

    with open(outname, "w") as fh:
        for i, a in enumerate(answers, 1):
            fh.write("Case #%i: %s\n" % (i, a))

if __name__ == "__main__":
    main()
