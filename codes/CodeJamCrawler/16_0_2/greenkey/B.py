import fileinput


def revenge_of_the_pancakes(pancake_stack):
    moves = 0
    while '-' in pancake_stack:
        for i in range(len(pancake_stack)):
            if pancake_stack[i] != pancake_stack[0]:
                break
        i += 1
        pancake_stack = ('-' if pancake_stack[0]=='+' else '+')*i + pancake_stack[i:]
        moves += 1


    return moves


lines = [l.strip() for l in fileinput.input()]
for (i, l) in enumerate(lines[1:]):
    print("Case #{}: {}".format(i + 1, revenge_of_the_pancakes(l)))
