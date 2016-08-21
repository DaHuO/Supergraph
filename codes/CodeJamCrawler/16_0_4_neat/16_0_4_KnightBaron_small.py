FILENAME = "D-small-attempt0"
LINE_PER_CASE = 1
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME


def solve(lines):
    output = ""
    # Solve the problem
    k, c, s = lines[0].split(" ")
    k = int(k)
    c = int(c)
    s = int(s)

    for i in range(s):
        output += str(i + 1) + " "

    return output.strip()

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
