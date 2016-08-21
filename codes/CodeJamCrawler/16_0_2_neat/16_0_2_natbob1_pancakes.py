# Code Jam 2016 Qualification Round
# Problem B -- Revenge of the Pancakes


def solve(stack):
    stack += '+'
    last_pancake = None
    flips = 0

    for pancake in stack:
        #print(pancake)
        if last_pancake is None:
            last_pancake = pancake
        elif pancake != last_pancake:
            flips += 1
            last_pancake = pancake

    print(flips)
    return flips

print("Wake up pancakes!")

input_filename = "B-large.in"
output_filename = input_filename + ".output"

problems = []

# Read in problems
with open(input_filename, 'r') as input_file:
    for line in list(input_file)[1:]:
        print("Appending {}".format(line))
        problems.append(line.strip())

with open(output_filename, 'w') as output_file:
    for i, problem in enumerate(problems):
        print("Problem: {}".format(problem))
        solution = solve(problem)

        output_line = "Case #{}: {}".format(i + 1, solution)

        print(output_line)
        output_file.write(output_line + "\n")



