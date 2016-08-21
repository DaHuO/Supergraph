import sys

def solve(pancakes, flipped = 0):
    if pancakes == '-':
        return 1

    while True:
        current_index = 0
        first = pancakes[0]
        current_flips = 0
        is_solved = True
        for current in pancakes[1:]:
            if first != current:
                if current != '+':
                    is_solved = False
                flipped = flipped + 1

                before = pancakes
                if first == '+':
                    replace = '-'
                else:
                    replace = '+'
                pancakes = replace * (current_index + 1) + pancakes[current_index + 1:]
                current_flips = current_flips + 1
                break

            current_index = current_index + 1

        if is_solved and current_index == (len(pancakes) - 1) and pancakes[-1] != '-':
            return flipped
        elif is_solved and current_index == (len(pancakes) - 1) and pancakes[-1] == '-' and current_flips == 0:
            return flipped + 1


filename = 'input.txt'
if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, 'r') as f:
    data = f.read()

    data = data.split("\n")
    data.pop(0)

    case = 0
    for line in data:
        if line == '': continue
        case = case + 1

        print "Case #{}: {}".format(case, solve(line))


