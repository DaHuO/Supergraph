FILENAME = "A-small-attempt0"
LINES_PER_CASE = 1
INITIAL_LINES = 0
INPUT_FILE = "%s.in" % FILENAME
OUTPUT_FILE = "%s.out" % FILENAME


def preprocess(initials):
    preprocessed = dict()
    # Global calculation

    return preprocessed


def solve(initials, lines, preprocessed):
    output = ""
    # Solve the problem
    s = lines[0]

    lastwords = [s[0]]
    for char in s[1:]:
        tmp = list(lastwords)
        for word in tmp:
            lastwords.remove(word)
            lastwords.append(word + char)
            lastwords.append(char + word)

    # print sorted(lastwords)
    # raw_input()

    return sorted(lastwords)[-1]

if __name__ == '__main__':
    input_file = open(INPUT_FILE, "r")
    output_file = open(OUTPUT_FILE, "w")

    cases = int(input_file.readline())

    initial_lines = list()
    for _ in range(INITIAL_LINES):
        initial_lines.append(input_file.readline()[:-1])  # Remove newline

    preprocessed = preprocess(initial_lines)

    for case in range(1, cases + 1):  # Count case from 1, 2, ..., n
        input_lines = list()
        for i in range(LINES_PER_CASE):
            input_lines.append(input_file.readline()[:-1])  # Remove newline
        output_file.write("Case #%d: %s\n" % (
            case,
            solve(initial_lines, input_lines, preprocessed),
        ))

    input_file.close()
    output_file.close()
