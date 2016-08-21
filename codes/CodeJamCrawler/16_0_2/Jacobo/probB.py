filename = "B-large"

def stack_reducer(pancakes):
    new_stack = pancakes[0]
    previous_pancake = pancakes[0]
    for char in pancakes[1:]:
        if char != previous_pancake:
            new_stack += char
        previous_pancake = char
    return new_stack[:-1]

def stack_counter(pancakes):
    val = len(pancakes)
    if pancakes[-1] == '+':
        return val - 1
    return val


with open(filename + ".in", "r") as input:
    with open(filename + ".out", "w") as output:
        for case_num in range(1, int(input.readline()) + 1):
            output.write("Case #{}: ".format(case_num))
            pancakes = input.readline()
            num_flips = stack_counter(stack_reducer(pancakes))
            output.write("{}\n".format(num_flips))
