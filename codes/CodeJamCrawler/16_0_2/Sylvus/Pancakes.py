# Language       : Python 3
# Compiled Using : py_compile
# Version        : Python 3.4.3


def contract_line(l):
    new_line = l[0]
    for c in l:
        if new_line[-1] != c:
            new_line += c
    return new_line


with open("B-large.in") as f:
    data = f.readlines()

first = True
test_case_counter = 0
for line in data:
    if first:
        first = False;
        continue
    # Get rid of the \n at the end.
    line = line[:-1]
    line = contract_line(line)
    test_case_counter += 1
    if line[0] == "-" and line[-1] == "-":
        print("Case #" + str(test_case_counter) + ": " + str(len(line)))
    elif line[0] == "+" and line[-1] == "-":
        print("Case #" + str(test_case_counter) + ": " + str(len(line)))
    elif line[0] == "-" and line[-1] == "+":
        print("Case #" + str(test_case_counter) + ": " + str(len(line) - 1))
    else:
        print("Case #" + str(test_case_counter) + ": " + str(len(line) - 1))
