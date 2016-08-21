import sys

def input_parser(input_path):
    with open(input_path, 'r') as f:
        c = int(f.readline())
        for case in range(c):
            strs = f.readline().strip()
            yield case, (strs,)

def get_output_path(input_path):
    return input_path[:-2] + "out"

def output(f, s):
    print(s)
    f.write(s + "\n")

def merge_pancakes(pan):
    simple_pan = []
    last = None
    for char in pan:
        if char == last:
            continue
        simple_pan.append(char)
        last = char
    return simple_pan

def problem(pan):
    pan = merge_pancakes(pan)
    if pan[-1] == '+':
        del pan[-1]
    return len(pan)

def main():
    input_path = sys.argv[1]
    with open(get_output_path(input_path), 'w') as g:
        for case, data in input_parser(input_path):
            out = problem(*data)
            output(g, "Case #{}: {}".format(case+1, out))

if __name__ == "__main__":
    main()

