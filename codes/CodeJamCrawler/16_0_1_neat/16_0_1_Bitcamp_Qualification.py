def read(filename):
    f = open(filename, 'r')
    f.readline()
    cases = []
    for line in f:
        cases.append(int(line))

    f.close()
    return cases

def solve(cases):
    output = []
    for case in cases:
        current_number = case
        previous_number = None
        remaining_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        repeated = False

        while True:
            if current_number == previous_number:
                repeated = True
                break

            for digit in str(current_number):
                if digit in remaining_digits:
                    remaining_digits.remove(digit)

            if len(remaining_digits) == 0:
                break

            previous_number = current_number
            current_number += case

        if repeated:
            output.append("INSOMNIA")
        else:
            output.append(str(current_number))

    return output

def output(filename, answers):
    f = open(filename, 'w')
    lines = []
    for caseIdx in range(0, len(answers)):
        line = "Case #{}: {}\n".format((caseIdx + 1), answers[caseIdx])
        lines.append(line)

    # we need to remove the last newline character from the last test case
    last_line = lines[-1]
    last_line = last_line[:-1]
    lines[-1] = last_line

    f.writelines(lines)
    f.close()

cases = read("A-large.in")
answers = solve(cases)
output("qual.large.out", answers)