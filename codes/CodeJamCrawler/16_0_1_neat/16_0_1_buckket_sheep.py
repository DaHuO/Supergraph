def count_number(starting_number):
    if starting_number == 0:
        return "INSOMNIA"

    digits = set()
    counting_number = 0
    while len(digits) != 10:
        counting_number += starting_number
        for digit in [int(i) for i in str(counting_number)]:
            digits.add(digit)
    return counting_number

if __name__ == '__main__':
    with open("input", "r") as input_file, open("output", "w") as output_file:
        next(input_file)
        case = 1
        for starting_number in input_file.readlines():
            output_file.write("Case #{0}: {1}\n".format(case, count_number(int(starting_number))))
            case += 1
