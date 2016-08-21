# Google Code Jam 2016
# Qualification - Revenge of the pancakes
# Tejas Deshpande - tejasd
# 04/09/2016


def num_ops(given_list, num_ops=0):
    while(True):
        given_list = trim_list(given_list)
        if len(given_list) == 0:
            return num_ops

        # if the first is a +, find the largest contiguous +s, flip them all to -s
        if given_list[0] == '+':
            given_list = flip_pancake_stack(given_list, find_first_negative_index(given_list))
            num_ops = num_ops + 1

        # flip the whole stack of pancakes
        given_list = flip_pancake_stack(given_list, len(given_list))
        num_ops = num_ops + 1


def flip_pancake_stack(given_list, end_pos):
    flipped_section = given_list[:end_pos]
    unflipped_section = given_list[end_pos:]
    flipped_section.reverse()

    for i in range(len(flipped_section)):
        if flipped_section[i] == '-':
            flipped_section[i] = '+'
        else:
            flipped_section[i] = '-'

    return flipped_section + unflipped_section


def find_first_negative_index(given_list):
    for i in range(len(given_list)):
        if given_list[i] == '-':
            return i

    return len(given_list)



def trim_list(given_list):
    for i in range(len(given_list) - 1, -1, -1):
        if given_list[i] == '-':
            return given_list[:i+1]

    return []

if __name__ == "__main__":
    num_test_cases = input()
    for i in range(int(num_test_cases)):
        list_pancakes = input()
        print('Case #' + str(i+1) + ': ' + str(num_ops(list(list_pancakes))))
