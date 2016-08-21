import sys

MAX = 100
PROBLEM = 'pancakes'


def pancakes(nm):
    sub_strings = nm.replace('-+', '-,+').replace('+-', '+,-').split(',')
    parsed_strings = map(lambda x: [x[0], len(x)], sub_strings)
    flips = 0

    # Keep flipping until there's nothing left to flip
    while len(parsed_strings) > 1:
        parsed_strings[1][1] = parsed_strings[1][1] + parsed_strings[0][1]
        flips = flips + 1
        parsed_strings = parsed_strings[1:]

    # There is one flip left if the remaining elements are -
    if parsed_strings[0][0] == '-':
        return flips + 1
    else:
        return flips


def main():
    if len(sys.argv) == 1:
        print (PROBLEM + '.py usage: python ' + PROBLEM + '.py <test case> ')
        sys.exit(-1)
    else:
        result = ''
        with open(sys.argv[1]) as f:
            lines = f.read().splitlines()
            num_tests = int(lines[0])
            tests = lines[1:num_tests + 1]

            for i, t in enumerate(tests):
                result = result + 'Case #' + str(i+1) + ": " + str(pancakes(t))
                if i + 1 < len(tests):
                    result = result + '\n'
        out = file('output-' + PROBLEM + '.out', 'w')
        out.write(result)
        out.close()


if __name__ == "__main__":
    main()
