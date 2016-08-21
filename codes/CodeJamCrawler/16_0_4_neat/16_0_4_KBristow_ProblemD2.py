import math


def process_line(line):
    line_split = line.split()
    initial_length = long(line_split[0])
    art_level = long(line_split[1])
    guess_limit = long(line_split[2])

    guesses_required = initial_length
    base_guesses = initial_length
    base_positions = range(1, initial_length + 1)
    if initial_length == 1:
        return str(1)
    elif initial_length == 2 and art_level > 1:
        return str(2)

    if guesses_required > guess_limit:
        return "IMPOSSIBLE"
    else:
        output = ""
        # block_size = long(math.pow(initial_length, art_level - 1))
        for num in base_positions:
            output += str(num) + " "
        return output.strip()


def find_level_one_guess(initial_length):
    required_guesses = initial_length - 1
    guess_positions = []
    for i in range(0, required_guesses):
        guess_positions += [2 + i * (initial_length + 1)]

    return required_guesses, guess_positions

year = 2016
problem_set = "SmallD"

with open(problem_set, 'r') as file_handle:
    lines = file_handle.readlines()


output_str = ""
for i in range(1, len(lines)):
    output_str += "Case #" + str(i) + ": " + str(process_line(lines[i])) + "\n"


output_str = output_str.strip()
print output_str
with open(str(year) + problem_set + ".out", "w") as file_handle:
    file_handle.write(output_str)


