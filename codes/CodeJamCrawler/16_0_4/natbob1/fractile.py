# Code Jam 2016 Qualification Round
# Problem D -- Fractiles

import math


def solve(k, c, s):
    if math.ceil(k / c) > s:
        return False

    tiles = []

    kk = 0
    while kk < k:
        tile_postition = 0

        for cc in reversed(range(c)):
            if kk == k:
                break

            tile_postition += kk * (k ** cc)
            print("kk = {}; cc = {}; k ** cc = {}; tile_position = {}".format(kk, cc, k ** cc, tile_postition))

            kk += 1

        tiles.append(tile_postition + 1)

    return tiles

print("Wake up tiles!")

input_filename = "D-large.in"
output_filename = input_filename + ".output"

problems = []

# Read in problems
with open(input_filename, 'r') as input_file:
    for line in list(input_file)[1:]:
        print("Appending {}".format(line))
        line = line.strip()

        problems.append(list(map(int, line.split())))

with open(output_filename, 'w') as output_file:
    for i, problem in enumerate(problems):
        print("Problem: {}".format(problem))
        solution = solve(*problem)

        solution_o = 'IMPOSSIBLE' if solution is False else ' '.join(map(str, solution))

        output_line = "Case #{}: {}".format(i + 1, solution_o)

        print(output_line)
        output_file.write(output_line + "\n")