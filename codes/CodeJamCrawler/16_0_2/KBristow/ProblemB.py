def process_line(line):
    line = line.strip()
    found_plus = False
    flips = 0
    for i in range(0, len(line)):
        char = line[i]
        if char == "-" and i + 1 < len(line) and line[i+1] == "+":
            flips += get_flips(found_plus)
            found_plus = True
        elif i+1 == len(line):
            if char == "-":
                flips += get_flips(found_plus)
        elif char == "+":
            found_plus = True
    return flips


def get_flips(found_plus):
    if found_plus:
        return 2
    else:
        return 1


year = 2016
problem_set = "LargeB"

with open(problem_set, 'r') as file_handle:
    lines = file_handle.readlines()


output_str = ""
for i in range(1, len(lines)):
    output_str += "Case #" + str(i) + ": " + str(process_line(lines[i])) + "\n"


output_str = output_str.strip()
print output_str
with open(str(year) + problem_set + ".out", "w") as file_handle:
    file_handle.write(output_str)


