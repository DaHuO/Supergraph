from fractions import gcd

FILENAME = "A-large"
LINE_PER_CASE = 1
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME
LIMIT = 9223372036854775807


def solve(lines):
    output = ""
    # Solve the problem
    n = int(lines[0])

    if n == 0:
        return "INSOMNIA"

    flags = []
    counter = 1
    while len(flags) < 10:
        if counter > LIMIT:
            return "INSOMNIA"
        output = counter * n
        digits = str(output)
        for digit in digits:
            if digit not in flags:
                flags.append(digit)
        counter += 1

    # print flags
    return output

if __name__ == '__main__':
    input_file = open(INPUT_FILE, "r")
    output_file = open(OUTPUT_FILE, "w")

    cases = int(input_file.readline())
    for case in range(1, cases + 1):  # Count case from 1, 2, ..., n
        input_lines = list()
        for i in range(LINE_PER_CASE):
            input_lines.append(input_file.readline()[:-1])  # Remove newline
        output_file.write("Case #%d: %s\n" % (
            case,
            solve(input_lines),
        ))

    input_file.close()
    output_file.close()
