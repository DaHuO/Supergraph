from collections import deque

def flip_bit(x):
    if x == "+": return "-" 
    else: return "+"

def flip_array(array, index):
    part_array = array[:index]
    part_array.reverse()
    return list(map(flip_bit, part_array)) + array[index:]

def are_all_flipped(array):
    for i in array:
        if i == "-": return False
    return True

def flip_pancakes(pancakes):

    if are_all_flipped(pancakes): return 0

    seen_items = set()
    queue = deque()
    current_pancake_stack = [pancakes, 0]

    while True:

        for i in range(len(current_pancake_stack[0]) + 1):
            flipped = flip_array(current_pancake_stack[0], i)

            if str(flipped) not in seen_items:
                if (are_all_flipped(flipped)):
                    return current_pancake_stack[1] + 1
                seen_items.add(str(flipped))
                queue.append([flipped, current_pancake_stack[1] + 1])

        current_pancake_stack = queue.popleft()


def read_file_and_output(filename):

    input_file = open(filename, "r")
    output_file = open("out.txt", "w")
    line_index = 1
    for line in input_file.readlines()[1:]:
        res = flip_pancakes(list(line))
        output_file.write("Case #" + str(line_index) + ": " + str(res) + "\n")
        line_index += 1

read_file_and_output("B-small-attempt0.in")
#pancakes = "+-+-+-+-+-+-+-"
#print("\n".join([str(flip_pancakes(list(x))) for x in ["-", "-+", "+-", "+++", "--+-"]]))
#print("moves:", flip_pancakes(list(pancakes)))
