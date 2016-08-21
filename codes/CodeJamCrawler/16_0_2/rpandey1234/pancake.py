import sys


def is_all_happy(pancakes):
    return pancakes[0] == '+' and len(set(pancakes)) == 1


def get_leading_same_state(pancakes):
    start_state = pancakes[0]
    count = 0
    for i in range(len(pancakes)):
        if pancakes[i] == start_state:
            count += 1
        else:
            break
    return count


def flip_pancake(state):
    if state == '+':
        return '-'
    else:
        return '+'


# Flip the first count pancakes in the pancakes list
def flip(count, pancakes):
    for i in range(count):
        pancakes[i] = flip_pancake(pancakes[i])


def compute_optimal_number(pancakes):
    if len(pancakes) == 0:
        return 0
    # print pancakes
    operations = 0
    while not is_all_happy(pancakes):
        operations += 1
        same_count = get_leading_same_state(pancakes)
        flip(same_count, pancakes)
        # print pancakes
    return operations


def main(filename):
    with open(filename) as f:
        num_entries = int(f.readline())
        for i in range(num_entries):
            pacake_stack = f.readline().strip()
            pancakes = []
            for ch in pacake_stack:
                pancakes.append(ch)
            solution = compute_optimal_number(pancakes)
            print "Case #" + str((i + 1)) + ": " + str(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "You should provide the input file name"
    else:
        main(sys.argv[1])
