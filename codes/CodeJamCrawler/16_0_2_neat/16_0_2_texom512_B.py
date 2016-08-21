__author__ = 'texom512'

t = int(input())

for i in range(t):
    stack = list(input())

    moves = 0
    # for _ in range(10):
    while '-' in stack:
        start_stack = list(stack)
        for elt, item in enumerate(stack):
            # print(stack, start_stack[0])
            if item == start_stack[0]:
                if item == '+':
                    stack[elt] = '-'
                else:
                    stack[elt] = '+'
            else:
                break
        # print(1, stack)
        moves += 1

        # if '-' not in stack:
        #     break

    print('Case #{}: {}'.format(i + 1, moves))
