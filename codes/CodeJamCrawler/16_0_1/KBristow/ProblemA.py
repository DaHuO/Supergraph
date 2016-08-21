def process_line(line):
    start_number = long(line)
    end_number, digits_seen = process_number(start_number)
    output = end_number
    if False in digits_seen:
        output = "INSOMNIA"

    return output


def process_number(number):
    digits_seen = [False] * 10
    current_number = number
    while False in digits_seen:
        num_str = str(current_number)
        for char in num_str:
            digits_seen[int(char)] = True
        if number + current_number == current_number:
            break
        current_number += number
    return current_number - number, digits_seen

year = 2016
problem_set = "LargeA"

with open(problem_set, 'r') as file_handle:
    lines = file_handle.readlines()


output_str = ""
for i in range(1, len(lines)):
    output_str += "Case #" + str(i) + ": " + str(process_line(lines[i])) + "\n"


output_str = output_str.strip()
print output_str
with open("C:\\Users\\Kieran\\Desktop\\" + str(year) + problem_set + ".out", "w") as file_handle:
    file_handle.write(output_str)


