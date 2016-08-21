#! /usr/bin/python
import sys

def is_valid_stack(stack):
    return all(map(lambda pancake: pancake == '+', stack))

def last_consecutive_index(stack, searched_sign, reversed=False):
    if reversed:
        stack = stack[::-1]

    last_index = -1
    for idx, sign in enumerate(stack):
        if sign != searched_sign:
            break
        else:
            last_index = idx

    if last_index > -1 and reversed:
        last_index = len(stack) - 1 - last_index

    return last_index


def flip_stack(stack):
    return map(lambda sign: '+' if sign == '-' else '-', stack)[::-1]

def perform_step(stack):
    if is_valid_stack(stack):
        return 0
    elif not stack:
        return 0

    steps_taken = 0
    # find suffix
    neg_suffix_end_idx = last_consecutive_index(stack, '-', True)
    if neg_suffix_end_idx > -1:
        # find prefix
        pos_prefix_end_idx = last_consecutive_index(stack, '+')

        if pos_prefix_end_idx > -1:
            # flip prefix
            steps_taken += 1
            stack = flip_stack(stack[:pos_prefix_end_idx + 1]) + stack[pos_prefix_end_idx+1:]

        # flip stack
        steps_taken += 1
        stack = flip_stack(stack)

    
    pos_suffix_end_idx = last_consecutive_index(stack, '+', True)
    if pos_suffix_end_idx > -1:
        return steps_taken + perform_step(stack[:pos_suffix_end_idx])
    else:
        return steps_taken + perform_step(stack)

if __name__ == '__main__':
    # get path to input file
    data_file = sys.argv[1]

    # load input data
    with open(data_file) as fd:
        fd.readline()
        stacks = [list(n.strip('\n')) for n in fd]

    results = map(perform_step, stacks)



    
    with open('pancake_revenge.txt', 'w') as fd:
        for idx, result in enumerate(results):
            fd.write('Case #{}: {}\n'.format(idx+1, result))
            print 'Case #{}: {}'.format(idx+1, result)


