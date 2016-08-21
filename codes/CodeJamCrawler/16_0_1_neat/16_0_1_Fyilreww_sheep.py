def count_sheep(initial_number):
    if initial_number == 0: return "INSOMNIA"
    seen_nums = set()
    index = 1
    current_number = initial_number
    while len(seen_nums) < 10:
        current_number = index * initial_number
        seen_nums = seen_nums.union(list(str(current_number)))
        index += 1
    return current_number


def read_file_and_output(filename):

    input_file = open(filename, "r")
    output_file = open("out.txt", "w")
    line_index = 1
    for line in input_file.readlines():
        res = count_sheep(int(line))
        output_file.write("Case #" + str(line_index) + ": " + str(res) + "\n")
        line_index += 1

read_file_and_output("A-large.in")

