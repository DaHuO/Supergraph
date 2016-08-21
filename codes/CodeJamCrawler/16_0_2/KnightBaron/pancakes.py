FILENAME = "B-large"
LINE_PER_CASE = 1
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME


def solve(lines):
    output = ""
    stack = str(lines[0])

    print "INPUT: %s" % stack

    # Already happy!
    if "-" not in stack:
        return 0

    # Trim +
    if stack[-1] == "+":
        counter = 1
        while stack[-counter] == "+":
            counter += 1
        stack = stack[:1 - counter]
        print "TRIMMED: %s" % stack

    pointer = stack[0]
    counter = 1
    for pancake in stack:
        if pancake != pointer:
            counter += 1
            pointer = pancake
    print "COUNTER: %d" % counter

    return counter

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
