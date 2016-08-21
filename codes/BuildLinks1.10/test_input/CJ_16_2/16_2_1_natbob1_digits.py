# Code Jam 2016 Round 1
# Problem A -- Getting the Digits

import collections

lookup = {
    "ZERO": 0,
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9
}

passes = [{
    "Z": "ZERO",
    "W": "TWO",
    "U": "FOUR",
    "X": "SIX",
    "G": "EIGHT"
}, {
    "O": "ONE",
    "H": "THREE",
    "F": "FIVE",
}, {
    "V": "SEVEN",
    "I": "NINE"
}]

def remove_word_from_letters(word, letters):
    print("Subtracting {}".format(word))
    return letters - collections.Counter(word)

def solve(letters):
    numbers = []
    pasn = 0
    removed = True

    while len(letters) != 0:
        if removed is True:
            removed = False
            pas = passes[pasn]
            for letter in pas:
                print(letters)

                if len(letters) == 0:
                    break

                if letter in letters:
                    removed = True
                    numbers.append(lookup[pas[letter]])
                    letters = remove_word_from_letters(pas[letter], letters)
        else:
            removed = True
            pasn += 1

    return "".join(map(str, sorted(numbers)))

input_filename = "A-large.in"
output_filename = input_filename + ".output"

problems = []

# Read in problems
with open(input_filename, 'r') as input_file:
    for line in list(input_file)[1:]:
        print("Appending {}".format(line))
        problems.append(collections.Counter(line[:-1]))

# Write out solutions
with open(output_filename, 'w') as output_file:
    for i, problem in enumerate(problems):
        solution = solve(problem)

        output_line = "Case #{}: {}".format(i + 1, solution)

        print(output_line)
        output_file.write(output_line + "\n")







