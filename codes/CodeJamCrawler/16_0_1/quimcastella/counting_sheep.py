import sys

def input_parser(input_path):
    with open(input_path, 'r') as f:
        c = int(f.readline())
        for case in range(c):
            num = int(f.readline())
            yield case, (num)

def get_output_path(input_path):
    return input_path[:-2] + "out"

def output(f, s):
    print(s)
    f.write(s + "\n")

def problem(num):
    digits_left = set(map(str,range(10)))
    sum_value = 0
    if num == 0:
        return 'INSOMNIA'
    for i in range(1000000):
        sum_value += num
        for s in str(sum_value):
            if s in digits_left:
                digits_left.remove(s)
                if not digits_left:
                    return sum_value
    print('LIMIT EXCEEDED')
    sys.exit()

def main():
    input_path = sys.argv[1]
    with open(get_output_path(input_path), 'w') as g:
        for case, data in input_parser(input_path):
            out = problem(data)
            output(g, "Case #{}: {}".format(case+1, out))

if __name__ == "__main__":
    main()

