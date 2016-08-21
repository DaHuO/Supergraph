

def print_output():
    '''() -> None
    retrieves the dictionary with results from read_input, and stores the
    results in the correct format in the file results.txt.
    '''
    results_dic = read_input()  # get results in form of a dic
    num_cases = results_dic[0]  # get number of cases in results
    write_file = open('results.txt', 'w')  # create results file
    for i in range(1, num_cases+1):  # cycle cases, printing results to file
        write_file.write("Case #{0}: {1}{2}".format(i, results_dic[i], "\n"))
    write_file.close()  # close results file


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
        value = int(line.strip('\n'))
        if(case == 0):  # check if line informing of number of cases
            results[case] = value
        else:  # solve problem for current case
            results[case] = get_last_num(value, value, set())
        case += 1
    input_file.close()  # close input file
    return results  # return results in form of dict case: answer


def get_last_num(n, N, numbers_seen):
    '''(int, int, set) -> str or int
    Takes the starting n value(twice, only for the start) and an empty set.
    Then cycles through multiples of n, by adding N each time to it, until
    all numbers {0,1,2,...,9} have been seen at least once. If that is
    impossible, 'INSOMNIA' is returned. Otherwise, the n value at which it
    occurs is returned.
    >>> get_last_num(0,0,set())
    INSOMNIA
    >>> get_last_num(11,11,set()):
    110
    >>> get_last_num(1,1,set()):
    10
    REQ: n must equal N ONLY when the function is called for the FIRST time
    REQ: numbers_seen must be an empty set when function is called first time
    '''
    # base case(s)
    # she never sleeps
    if(N == 0):
        return "INSOMNIA"
    # she has spotted all 10 numbers and is now asleep
    elif(len(numbers_seen) == 10):
        return n-N  # subtract N because we check before we cycle the ---
    # --- current numbers possibilities
    # she still has as atleast 1 number to go
    else:
        for i in range(len(str(n))):  # cycle through individual nums
            numbers_seen.add(int(str(n)[i]))  # add to set
        return get_last_num(n+N, N, numbers_seen)  # go to next multiple of n


if(__name__ == '__main__'):
    print_output()
