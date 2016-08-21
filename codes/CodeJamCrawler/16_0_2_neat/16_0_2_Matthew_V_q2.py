def flip_pancakes(stack, count=0):
    '''(str) -> int
    Takes a string representing pancake sides ('-' or '+') and performs the
    least amount of flips on the string for all pancakes to be face side up(+).
    Returns the number of flips.
    >>> flip_pancakes('-')
    1
    >>> flip_pacakes('-+')
    1
    >>> flip_pancakes('+-')
    2
    >>> flip_pancakes('+++')
    0
    REQ: stack must contain only '-'s and '+'s
    '''
    if(stack == ''):  # if stack is empty
        return count
    if(stack.count('-') == 0):  # if stack already flipped up
        return count
    else:
        # get flip index
        flip_ind = get_flip_index(stack)
        stack = flip_stack(stack[:flip_ind])  # flip at index
        count += 1  # increase count of flips
        return flip_pancakes(stack, count)  # repate until all flipped


def get_flip_index(stack):
    '''(str) -> int
    Takes a stack, and returns the index of the last '-' in it.
    >>> get_flip_index('--++-+')
    4
    REQ: stack must only be '-'s and '+'s
    '''
    count = len(stack) - 1  # count from end of string forwards, looking for -
    while(count >= 0 and stack[count] == '+'):
        count -= 1
    return count


def flip_stack(stack):
    '''(str) -> str
    Takes a string of '-'s and '+'s and flips them.
    >>> flip_stack('--++-+')
    ++--+-
    REQ: stack must only contain '+'s and '-'s
    '''
    # flip the '-'s with '+'s
    new_stack = stack.replace("-", "#").replace("+", "-").replace("#", "+")
    return new_stack


def read_input():
    '''() -> dict
    Reads the input file, then calls get_last_num for each line, and stores
    the result associated with each case number in an array. The value
    associated with the key 0 is the number of cases in the dictionary.
    '''
    input_file = open('input.in', 'r')  # open file to read
    case = 0  # keep track of what case input we are reading
    results = {}  # store results for each case
    for line in input_file:  # read input file
        value = str(line.strip('\n'))
        if(case == 0):  # check if line informing of number of cases
            results[case] = value
        else:  # solve problem for current case
            results[case] = flip_pancakes(value)
        case += 1
    input_file.close()  # close input file
    return results  # return results in form of dict case: answer


def print_output():
    '''() -> None
    retrieves the dictionary with results from read_input, and stores the
    results in the correct format in the file results.txt.
    '''
    results_dic = read_input()  # get results in form of a dic
    num_cases = results_dic[0]  # get number of cases in results
    write_file = open('results.txt', 'w')  # create results file
    for i in range(1, int(num_cases)+1):  # cycle cases, printing to file
        write_file.write("Case #{0}: {1}{2}".format(i, results_dic[i], "\n"))
    write_file.close()  # close results file


if(__name__ == '__main__'):
    print_output()
