__author__ = 'Jiranun.J'

n_test_case = int(raw_input())  # read a line with a single integer

def flip(pancakes, indx):
    top_stack = pancakes[0:indx+1]
    conv_top = [0 if i == 1 else 1 for i in top_stack]
    bottom_stack = pancakes[indx+1:len(pancakes)]
    result = []
    result.extend(conv_top[::-1])
    result.extend(bottom_stack)
    return result

def get_number_of_flip(pancakes):
    # print pancakes
    if not any(pancakes):
        return 1
    elif all(pancakes):
        return 0
    else:
        rev_stack = pancakes[::-1]
        for i in range(len(rev_stack)):
            if rev_stack[i] == 0:
                break
        if i != 0:
            return get_number_of_flip(pancakes[0: len(pancakes)-i])
        else:
            top_face = pancakes[0]
            for i in range(len(rev_stack)):
                if rev_stack[i] == top_face:
                    return 1+get_number_of_flip(flip(pancakes, len(pancakes) - i - 1))
                    break

for i in range(n_test_case):
    inpt_pnck = raw_input()
    pancakes = []
    for c in inpt_pnck:
        if c == '-':
            pancakes.append(0)
        elif c == '+':
            pancakes.append(1)
    print 'Case #'+str(i+1)+': '+str(get_number_of_flip(pancakes))

