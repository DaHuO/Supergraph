import os, sys

SMALL_INPUT = 'small.txt'
LARGE_INPUT = 'large.txt'
EXAMPLE_INPUT = 'example.txt'
EXTRA_EXAMPLE = 'extra_example.txt'

INPUT_FILE = [EXAMPLE_INPUT, SMALL_INPUT, LARGE_INPUT, EXTRA_EXAMPLE]


def process_input(input_raw):
    num_cases = int(input_raw.pop(0))
    cases = [i.strip('\n') for i in input_raw]
    return num_cases, cases


def get_output(N):
    numbers_encountered = set()
    N = int(N)
    if N == 0:
        return "INSOMNIA"
    count = N
    while len(numbers_encountered)<10:
        numbers_encountered = numbers_encountered | set(str(count))
        if len(numbers_encountered) == 10:
            return count
        count += N
    return "INSOMNIA"



if __name__ == "__main__":
    VERBOSE = False
    input_file_index = sys.argv[1] if len(sys.argv) > 1 else 1
    input_file = os.path.join("input", INPUT_FILE[input_file_index])
    with open(input_file, 'r') as f:
        input_data_raw = f.readlines()

    num_cases, cases = process_input(input_data_raw)

    output_array = []
    for case_number in xrange(num_cases):
        if VERBOSE:
            print "Running Problem", case_number
            print "\tInput: ", cases[case_number]
        output_array.append("Case #{}: {}".format(str(case_number+1), str(get_output(cases[case_number]))))
        if VERBOSE:
            print "\tOutput: ", output_array[-1]

    output_txt = "\n".join(output_array)
    output_file = os.path.join("output", INPUT_FILE[input_file_index])

    with open(output_file, 'w+') as f:
        f.write(output_txt)

    print "Done"

