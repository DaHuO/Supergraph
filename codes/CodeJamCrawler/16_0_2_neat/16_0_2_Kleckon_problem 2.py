input_file = open("B-large.in")
output_file = open("B-large-output.txt", "w")

case_number = 1
cases = input_file.readlines()
for n in cases[1:len(cases)]:
    stack = n.strip()
    list_stack = list()
    for char in stack:
        list_stack.append(char)

    sign_changes = 0
    flips = 0

    if list_stack[0] == "-":
        if "+" not in list_stack:  # all "-"
            flips = 1
        else:
            if list_stack[len(list_stack) - 1] == "-":
                sign_changes += 1
            for i in range(0, len(list_stack) - 1):
                if list_stack[i] == "-" and list_stack[i+1] == "+":
                    sign_changes += 1
            flips = sign_changes * 2 - 1

    if list_stack[0] == "+":
        if "-" not in list_stack:  # all "+"
            flips = 0
        else:
            for i in range(0, len(list_stack) - 1):
                if list_stack[i] == "+" and list_stack[i+1] == "-":
                    sign_changes += 1
            flips = sign_changes * 2
    output_file.write("Case #{0}: {1}\n".format(case_number, flips))
    case_number += 1

input_file.close()
output_file.close()
