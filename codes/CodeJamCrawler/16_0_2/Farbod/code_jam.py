def flip(sel):
    sel = list(sel)  # turns it into a list

    for i in range(len(sel)):
        # replaces chars
        sel[i] = ("+" if sel[i] == "-" else "-")

    replaced = "".join(sel)  # turns it into a string
    return replaced[::-1]  # reverses the string


reading_filename = "B-large.in"
writing_filename = "output-large.txt"


with open(reading_filename, "r") as file:
    contents = file.readlines()

with open(writing_filename, "w+") as file:
    tests = contents[0]
    print("Number of tests: {0}".format(tests))

    for case in range(1, int(tests)+1):
        s = contents[case].strip("\n")

        if ("+" in s) and ("-" not in s):
            # print("Case #{0}: {1}\n".format(str(case), "0"))
            file.write("Case #{0}: {1}\n".format(str(case), "0"))
            continue
        elif ("-" in s) and ("+" not in s):
            # print("Case #{0}: {1}\n".format(str(case), "1"))
            file.write("Case #{0}: {1}\n".format(str(case), "1"))
            continue

        stack = s
        maneuvers = 0
        while True:
            # print("- Working out: " + stack)

            if ("+" in stack) and ("-" not in stack):
                file.write("Case #{0}: {1}\n".format(str(case), str(maneuvers)))
                break
            elif ("-" in stack) and ("+" not in stack):
                file.write("Case #{0}: {1}\n".format(str(case), str(maneuvers + 1)))
                break

            if stack[0] == "+":
                last_minus = stack.find("-")
            else:
                last_minus = stack.find("+")

            selection = stack[:last_minus]
            inverse_sel = stack[last_minus:]

            # print("Selection: " + selection)

            # noinspection PyTypeChecker
            new_selection = flip(selection)
            # print("new selection " + new_selection)

            new_stack = new_selection + inverse_sel

            stack = new_stack
            maneuvers += 1
