from io import open


def count(init_number):
    input_int = int(init_number.rstrip())

    if input_int == 0:
        return "INSOMNIA"

    filter_set = set(str(input_int))
    result = input_int
    increment = 2
    while len(filter_set) < 10:
        result = input_int * increment
        filter_set = filter_set | set(str(result))
        increment += 1

    return result


INPUT_FILE_NAME = 'A-large.in'
OUTPUT_FILE_NAME = 'output.txt'
input_file = open(INPUT_FILE_NAME, 'r')
output_file = open(OUTPUT_FILE_NAME, 'w')

case = 1
with input_file as file:
    limit = int(next(file).rstrip())
    for case in range(1, limit + 1):
        count_result = count(file.readline())
        print(count_result)
        output_file.writelines("Case #" + str(case) + ": " + str(count_result) + "\n")

input_file.close()
output_file.close()
