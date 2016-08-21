def get_input(f, num_cases, lines_per_case, transforms, add_lines):
    
    case_inputs = []

    for case in range(num_cases):
        case_input = []
        
        case_lines = lines_per_case
        if lines_per_case < 0:
            first_line  = f.readline().strip().split()
            case_lines = int(first_line[lines_per_case])
            case_input.append(' '.join(first_line))

        case_lines += add_lines

        for i in range(case_lines):
            if lines_per_case < 0:
                case_input.append(f.readline().strip().split())
            else:
                case_input.append(transforms[i](f.readline().strip()))

        case_inputs.append(case_input)

    return case_inputs

def get_output_string(case, ans):
    return 'Case #' + str(case) + ': ' + str(ans) + '\n'

def print_output(fw, numCases, case_inputs, get_ans):
    for case in range(1, numCases + 1):
        fw.write(get_output_string(case, get_ans(case_inputs[case-1])))

def process(fname, num_lines, transforms, get_ans, add_lines = 0):
    """Process the input to calculate and write out the correct output
    
    fname --  The name of the input file
    num_lines -- The number of lines PER case
    transforms -- The transforms to apply to each line of a case
    get_ans -- The method that takes a case as an input and returns the output for the case
    """
    with open(fname) as fr, open(fname + '.out', 'w') as fw:
        num_cases = int(fr.readline().strip())
        case_inputs = get_input(fr, num_cases, num_lines, transforms, add_lines)
        print_output(fw, num_cases, case_inputs, get_ans)
