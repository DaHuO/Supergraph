import sys

MAX = 100


def bleatrix(nm):
    digits = set()
    for i in range(1, MAX+1):
        for d in str(i * nm):
            digits.add(d)
            if len(digits) == 10:
                return str(i * nm)
    return 'INSOMNIA'


def main():
    if len(sys.argv) == 1:
        print 'beatrix.py usage: python beatrix.py <test case> '
        sys.exit(-1)
    else:
        result = ''
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()
            num_tests = int(lines[0])
            tests = map(lambda x: int(x), lines[1:num_tests + 1])

            for i, t in enumerate(tests):
                result = result + 'Case #' + str(i+1) + ": " + bleatrix(t)
                if i + 1 < len(tests): 
                    result = result + '\n'
        out = file('output-bleatrix.out', 'w')
        out.write(result)
        out.close()


if __name__ == "__main__":
    main()
