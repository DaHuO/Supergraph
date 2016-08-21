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

if __name__ == "__main__":
    #output_str = answer_problem(sys.argv[1], solve_a)
    output_str = answer_problem(sys.argv[1], solve_b)
    with open(sys.argv[1].replace('.in', '.out'), 'w') as f:
        f.write(output_str)
