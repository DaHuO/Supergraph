def openfile(input_file):
    """
    Open a file location given as a function parameter and return a list of strings containing lines in the file.
    :param input_file: file location of file to be opened
    :return: my_list: list of strings containing lines in the file
    """
    with open(input_file) as f:
        my_list = f.read().splitlines()
    return my_list


def flip_pancakes(pancake_stack):
    flips = 1
    # reverse pancake stack to make indexing easier
    reversed_pancake_stack = pancake_stack[::-1]
    # find first '-' symbol
    first_minus = reversed_pancake_stack.find('-')
    # if no '-' no flips needed
    if first_minus == -1:
        return 0
    # count number of bit flips from that point onward
    else:
        for idx in range(first_minus, len(reversed_pancake_stack)-1):
            if reversed_pancake_stack[idx] != reversed_pancake_stack[idx+1]:
                flips += 1
    return flips

if __name__ == '__main__':
    # read input
    input_list = openfile('B-small-attempt0.txt')
    # open output file
    f = open('B-small-solution0.txt', 'w')
    num_cases = int(input_list[0])
    # iterate through cases
    for i in range(1, num_cases + 1):
        ans = flip_pancakes(input_list[i])
        f.write('Case #{0}: {1}\n'.format(i, ans))