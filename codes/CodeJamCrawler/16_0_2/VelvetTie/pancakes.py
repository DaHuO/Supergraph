import sys

def flip(to_flip):
    """

    >>> flip('-')
    '+'

    >>> flip('+')
    '-'

    >>> flip('+++')
    '---'

    >>> flip('-+')
    '-+'

    >>> flip('--+')
    '-++'

    :param to_flip:
    :return:
    """
    num_pancakes = len(to_flip)
    flipped = [0 for i in range(num_pancakes)]
    for i in range(num_pancakes):
        if to_flip[i] == '-':
            flipped[num_pancakes - 1 - i] = '+'
        else:
            flipped[num_pancakes - 1 - i] = '-'

    return ''.join(flipped)


def count_flips(pancakes):
    """
    >>> count_flips('-')
    1

    >>> count_flips('+')
    0

    >>> count_flips('-+')
    1

    >>> count_flips('+-')
    2

    >>> count_flips('+++')
    0

    >>> count_flips('--+-')
    3

    :param pancakes - string
    """

    num_flips = 0
    if '-' not in pancakes:
        #print('No flips needed')
        return num_flips
    elif '+' not in pancakes:
        #print('Just flip once')
        pancakes = flip(pancakes)
        num_flips = 1
        return num_flips
    else:
        ref_sign = pancakes[0]
        to_flip = ''

        for p in pancakes:
            if p != ref_sign:
                break
            else:
                to_flip += p
        print("to_flip={}".format(to_flip), file=sys.stderr)
        flipped = flip(to_flip)
        num_flips += 1
        # Put together new pancake stack.
        num_flipped = len(flipped)
        new_stack = flipped + pancakes[num_flipped:]
        print("new_stack={}".format(new_stack), file=sys.stderr)
        num_flips += count_flips(new_stack)
        return num_flips

def read_input():
    num_test_cases = int(input())
    for t in range(1, num_test_cases + 1):
        pancakes = input()
        flips = count_flips(pancakes)
        print("Case #{}: {}".format(t, flips))

if __name__ == "__main__":
    read_input()
