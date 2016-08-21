def solve_string(pancakes):
    """
    Strategy:
        1. Reduce into groups.
        2. Count groups.
        3. Subtract one if the last one is +
    """
    p_groups = reduce_p(pancakes)
    if (p_groups[-1] == "+"):
        return len(p_groups) - 1
    else:
        return len(p_groups)

def reduce_p(pancakes):
    i = 1
    while i < len(pancakes):
        if (pancakes[i] == pancakes[i - 1]):
            pancakes = pancakes[:i] + pancakes[(i+1):]
        else:
            i += 1
    return pancakes

def solve(my_file):
    f = open(my_file + ".in", "r")
    g = open(my_file + ".out", "w")
    num_test_cases = int(f.readline())
    for case_no in range(1, num_test_cases + 1):
        case_input = f.readline().rstrip()
        case_output = solve_string(case_input)
        message = "Case #" + str(case_no) + ": " + str(case_output)
        print message
        g.write(message + "\n")
        
solve("B-large")
