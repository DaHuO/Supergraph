import itertools

print_result = True

# return a value corresponding to the output for case N. A newline will be appended automatically.
def do_case_N(case_N):
    mode = '+'
    score = 0

    for i in case_N[::-1]:
        if i != mode:
            score += 1
            mode = i

    return score

# this function is called once for each test case
def output_generator(input_file):
    num_cases = int(f.readline())
    for i in range(num_cases):
        case_N = input_file.readline().strip()
        result = do_case_N(case_N)
        result_string_line = 'Case #{}: {}\n'.format(i+1, result)
        if print_result:
            print(result_string_line, end='')
        yield result_string_line

f = open('input.txt')
out_f = open('output.txt','w')

out_f.writelines(output_generator(f))

