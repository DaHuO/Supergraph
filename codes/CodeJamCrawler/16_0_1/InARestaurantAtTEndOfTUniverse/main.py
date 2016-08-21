import argparse


def process_input(input_line):
    seen = []
    input = int(input_line)
    if input == 0:
        return "INSOMNIA"

    output = input
    i = input
    while True:
        while i >= 1:
            r = i % 10
            if r not in seen:
                # print("Appending {}".format(r))
                seen.append(r)
            i = int(i/10)

        if not len(seen) == 10:
            output += input
            i = output
        else:  # seen all digits
            break

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Input File.')
    parser.add_argument('f', metavar='file', help='Input file')
    args = parser.parse_args()
    file_name = args.f

    output_lines = []
    with open(file_name) as f:
        first_input_line = True
        for input_line in f:
            if first_input_line:  # skip number of test cases
                first_input_line = False
                continue

            input = input_line.strip()
            output = process_input(input)
            print("{} -> {}".format(input, output))
            output_lines.append(output)

    # write output file:
    f = open('output', 'w')
    i = 1
    for l in output_lines:
        f.write("Case #{}: {}\n".format(i, l))
        i += 1
