# Code Jam 2016 Qualification Round
# Problem A -- Counting Sheep


def solve(n):
    seen_digit_map = {}
    multiple = 0

    if n == 0:
        return False

    for i in range(10):
        seen_digit_map[i] = False

    while not all(seen_digit_map.values()):
        multiple += 1

        div_counter = 1
        n_multiple = n * multiple

        #print(seen_digit_map)

        while div_counter <= n_multiple:
            #print("n = {}; n_mul = {}; div_c = {}; out = {}".format(n, n_multiple, div_counter,
            #                                                        (n_multiple // div_counter) % 10))
            seen_digit_map[(n_multiple // div_counter) % 10] = True
            div_counter *= 10

    return n_multiple

print("Wake up sheeple!")

input_filename = "A-large.in"
output_filename = input_filename + ".output"

problems = []

# Read in problems
with open(input_filename, 'r') as input_file:
    for line in list(input_file)[1:]:
        problems.append(int(line))

with open(output_filename, 'w') as output_file:
    for i, problem in enumerate(problems):
        solution = solve(problem)
        solution_o = 'INSOMNIA' if solution is False else str(solution)

        output_file.write("Case #{}: {}\n".format(i + 1, solution_o))



