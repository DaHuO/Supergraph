import sys

def answer_problem(file_name, f_solve):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        output_str = '\n'.join(
            "Case #{0}: {1}".format(i+1, f_solve(input_str))
            for i, input_str in enumerate(f.read().splitlines()))
    return output_str



def solve_a(input_str):
    letters_seen = set()
    all_letters = set(str(x) for x in range(10))
    incr = int(input_str)
    if incr == 0:
        return "INSOMNIA"
    x = 0
    while letters_seen != all_letters:
        x += incr
        letters_seen |= set(str(x))
    return str(x)

def solve_b(input_str):
    num_flips = 0
    while input_str != '+' * len(input_str):
        if input_str.find('+') == -1:
            return num_flips + 1
        elif input_str.find('+') < input_str.find('-'):
            input_str = flip_n_pancakes(input_str, 
                                        input_str.find('-'))
        else:
            input_str = flip_n_pancakes(input_str, 
                                        input_str.find('+'))
        num_flips += 1
    return num_flips

def flip_n_pancakes(pancake_pile, n):
    return ''.join({'+':'-', '-': '+'}[x] for x in 
        pancake_pile[:n][::-1]) + pancake_pile[n:]


def answer_problem_special(file_name, f_solve):
    with open(file_name, 'r') as f:
        num_cases = int(f.readline())
        n, j = f.readline().split()
        return f_solve(n, j)

def solve_c(string_len, num_cases):
    output_str = "Case #1:\n"
    num_string = '1' * int(string_len)
    num_cases = int(num_cases)
    while num_cases:
        non_triv_divs = get_nontrivial_divisors(num_string)
        while not all(non_triv_divs):
            print("going down...", num_string)
            num_string = next_lowest_candidate(num_string)
            non_triv_divs = get_nontrivial_divisors(num_string)
        output_str += ' '.join([num_string] + 
            non_triv_divs) + '\n'
        print("got one!", num_string)
        num_string = next_lowest_candidate(num_string)
        num_cases -= 1
    return output_str

def get_nontrivial_divisors(num_string):
    return [find_str_divisor(str_base_n_to_int(num_string, i))
        for i in range(2, 11)]

def next_lowest_candidate(num_string):
    return '1' + int_to_str_binary(
        str_base_n_to_int(num_string[1:-1], 2) - 1) + '1'

def str_base_n_to_int(input_str, base):
    return sum(int(input_str[x]) * (base ** 
                (len(input_str) - 1 - x))
                for x in range(len(input_str)))

def int_to_str_binary(input_num):
    output_str = ""
    while input_num:
        input_num, i = divmod(input_num, 2)
        output_str = str(i) + output_str
    return output_str

def find_str_divisor(n):
    import math
    for i in xrange(2, 10000): #int(math.sqrt(n))):
        if n % i == 0:
            return str(i)
    return None

def solve_d(input_str):
    k, c, s = (int(x) for x in input_str.split())
    if c == 1:
        if s < k:
            return "IMPOSSIBLE"
        else:
            return ' '.join(str(x+1) for x in range(k))
    elif c > 1 and s < k / float(2):
        return "IMPOSSIBLE"
    else:
        output_list = [(2 * k * x) + (2 * (x + 1)) for x in range((k + 1) // 2)]
        if k % 2:
            output_list[-1] -= 1
        # Checking stuff
        #for x in get_all_single_gold(k, c):
        #    solved = False
        #    for y in output_list:
        #        if y > len(x):
        #            print("OVERSIZE!", x, len(x), y, input_str)
        #        if x[y-1] == 'G':
        #            solved = True
        #    if not solved:
        #        print("NOT SOLVED!", input_str, x, output_list)
        # Return
        return ' '.join(str(x) for x in output_list)


def get_all_single_gold(k, c):
    for i in range(k):
        pattern = ('L' * i) + 'G' + ('L' * (k - 1 - i))
        complex_pattern = pattern
        for j in range(c-1):
            complex_pattern = apply_complexity_plus_one(complex_pattern, pattern)
        yield complex_pattern

def apply_complexity_plus_one(last_complexity, orig_pattern):
    return ''.join({'G': len(orig_pattern) * 'G', 'L': orig_pattern}[x] for x in last_complexity)



if __name__ == "__main__":
    #output_str = answer_problem(sys.argv[1], solve_a)
    #output_str = answer_problem(sys.argv[1], solve_b)
    #output_str = answer_problem_special(sys.argv[1], solve_c)
    output_str = answer_problem(sys.argv[1], solve_d)
    with open(sys.argv[1].replace('.in', '.out'), 'w') as f:
        f.write(output_str)
