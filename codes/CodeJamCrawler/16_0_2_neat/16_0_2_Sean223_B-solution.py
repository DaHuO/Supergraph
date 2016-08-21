__author__ = 'sean'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

# IN_FILE = 'B-small.in'
# OUT_FILE = 'small_out.txt'

IN_FILE = 'B-large.in'
OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(numbCases):
    answer = ""

    input_line = next(it).strip()
    pancakes = [pancake == '+' for pancake in input_line]
    number_of_flips = 0

    while not all(pancakes):
        new_pancakes = pancakes[:]
        top_most_blank_pancake = pancakes.index(False)
        bottom_most_blank_pancake = max(index for index, happy in enumerate(pancakes) if not happy)

        del new_pancakes[bottom_most_blank_pancake+1:]

        if top_most_blank_pancake > 0:
            for i in range(0, top_most_blank_pancake):
                new_pancakes[i] = False
        else:
            for i in range(0, bottom_most_blank_pancake + 1):
                new_pancakes[bottom_most_blank_pancake - i] = not pancakes[i]  # Pancakes are reversed, and flipped

        number_of_flips += 1
        pancakes = new_pancakes

    line = "Case #{0}: {1}\n".format(str(case+1), str(number_of_flips))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
