import random



def openfile(input_file):
    """
    Open a file location given as a function parameter and return a list of strings containing lines in the file.
    :param input_file: file location of file to be opened
    :return: my_list: list of strings containing lines in the file
    """
    with open(input_file) as f:
        my_list = f.read().splitlines()
    return my_list


def count_sheep(n):
    """

    :param n:
    :return:
    """
    number_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    seen = set()
    multiplied_n = n

    for char in str(multiplied_n):
        seen.add(char)
    if seen.issuperset(number_set):
        return multiplied_n

    for i in range(0, n*100):
        multiplied_n += n

        for char in set(str(multiplied_n)):
            seen.add(char)

        if seen.issuperset(number_set):
            return multiplied_n

    return 0

if __name__ == '__main__':
    f = open('alarge_out.txt', 'w')
    input_deque = openfile('alarge_in.txt')
    num_cases = int(input_deque[0])
    for i in range(1, num_cases+1):
        ans = count_sheep(long(input_deque[i]))
        if ans == 0:
            f.write('Case #{0}: INSOMNIA\n'.format(i))
        else:
            f.write('Case #{0}: {1}\n'.format(i, ans))

