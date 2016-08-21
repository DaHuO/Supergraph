import argparse


def process_input(input_line):
    # Algorithm: count number of alternating + and - clusters in input_line, start counting
    # from the first - cluster on the right
    # so --+-- -> X X X -> 3
    # --+++--+--+++ -> X X X X X -> 5
    # --+--++--+ -> 5
    # step 1: remove pluses from right hand side:
    input = input_line
    index = input.rfind('-')
    if (index > -1):
        input = input[0:index+1]
    else:
        return 0

    # count number of clusters
    last_side = input[0]
    output = 1
    for side in input:
        if not side == last_side:
            output += 1
            last_side = side

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
