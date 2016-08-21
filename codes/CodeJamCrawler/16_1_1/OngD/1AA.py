from collections import deque


def openfile(input_file):
    """
    Open a file location given as a function parameter and return a list of strings containing lines in the file.
    :param input_file: file location of file to be opened
    :return: my_list: list of strings containing lines in the file
    """
    with open(input_file) as f:
        my_list = f.read().splitlines()
    return my_list


def last_word(n):
    ret = deque(n[0])
    n = n[1:]
    for char in n:
        if char >= ret[0]:
            ret.appendleft(char)
        else:
            ret.append(char)
    return ''.join(ret)

if __name__ == '__main__':
    # read input
    input_list = openfile('1aa_in.txt')
    # open output file
    out = open('1aa_out.txt', 'w')
    num_cases = int(input_list[0])
    # iterate through cases
    for i in range(1, num_cases + 1):
        ans = last_word(input_list[i])
        out.write('Case #{0}: {1}\n'.format(i, ans))