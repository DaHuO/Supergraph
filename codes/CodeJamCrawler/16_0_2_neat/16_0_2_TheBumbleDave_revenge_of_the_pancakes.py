def calculate_optimal_flips(stack_of_pancakes):
    pancake_height = stack_of_pancakes.__len__()
    happy_side = '+'
    blank_side = '-'
    optimal_flips = 0
    if blank_side not in stack_of_pancakes:
        return optimal_flips
    else:
        while pancake_height > 0:
            pancake_height -= 1
            if stack_of_pancakes[pancake_height] == blank_side:
                optimal_flips += 1
                if blank_side == '-':
                    blank_side = '+'
                    happy_side = '-'
                else:
                    blank_side = '-'
                    happy_side = '+'
    return optimal_flips

input_file = "B-large.in"
with open(input_file, 'r') as file_object_in:
    lines = file_object_in.readlines()
    testcases = int(lines[0].strip())
    case_number = 0
    output_file = "pancake_output.txt"

    while case_number < testcases:
        case_number += 1
        stack_of_pancakes = lines[case_number].strip()

        with open(output_file, 'a') as file_object_out:
            file_object_out.write("Case #" + str(case_number) + ": " + str(calculate_optimal_flips(stack_of_pancakes)) + "\n")