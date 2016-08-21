import sys


def answer_problem(file_name, f_solve):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        output_str = '\n'.join(
            "Case #{0}: {1}".format(i+1, f_solve(input_str))
            for i, input_str in enumerate(f.read().splitlines()))
    return output_str


def answer_problem_special(file_name, f_solve):
    with open(file_name, 'r') as f:
        num_cases = int(f.readline())
        n, j = f.readline().split()
        return f_solve(n, j)


def solve_a(input_str):
    bt_stack = [(input_str, [])]
    while bt_stack:
        curr = bt_stack.pop()
        if not curr[0]:
            return ''.join(str(x) for x in sorted(curr[1]))
        else:
            for i in range(10):
                parsed_digit = remove_num(curr[0], i)
                if parsed_digit[1]:
                    bt_stack += [(parsed_digit[0], parsed_digit[1] + curr[1])]


def remove_num(curr_str, num):
    num_str = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
               "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"][num]
    new_str = curr_str
    for c in num_str:
        str_index = new_str.find(c)
        if str_index == -1:
            return (curr_str, None)
        else:
            new_str = new_str[:str_index] + new_str[str_index+1:]
    return (new_str, [num])


if __name__ == "__main__":
    output_str = answer_problem(sys.argv[1], solve_a)
    #output_str = answer_problem(sys.argv[1], solve_b)
    #output_str = answer_problem_special(sys.argv[1], solve_c)
    #output_str = answer_problem(sys.argv[1], solve_d)
    with open(sys.argv[1].replace('.in', '.out'), 'w') as f:
        f.write(output_str)
