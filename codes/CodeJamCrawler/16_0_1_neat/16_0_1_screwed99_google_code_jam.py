import sys

def answer_problem(file_name, f_solve):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        output_str = '\n'.join(
            "Case #{0}: {1}".format(i+1, f_solve(input_str))
            for i, input_str in enumerate(f.readlines()))
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

if __name__ == "__main__":
    output_str = answer_problem(sys.argv[1], solve_a)
    with open(sys.argv[1].replace('.in', '.out'), 'w') as f:
        f.write(output_str)



#print(answer_problem('A-small-attempt0.in', solve_a))
#for x in range(1, 1000000):
#    if not solve_a(str(x)):
#        print("PROBLEM")
