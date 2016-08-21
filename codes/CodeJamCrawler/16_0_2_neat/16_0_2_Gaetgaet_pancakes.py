T = int(input())


def alg(stack):
    last_char = ''
    num_flips = 0
    for char in stack:
        if char == last_char:
            pass
        else:
            if char == '-':
                if last_char == '':
                    num_flips += 1
                else:
                    num_flips += 2
                last_char = '-'
            if char == '+':
                last_char ='+'
    return num_flips



for t in range(T):
    stack = input()
    print('Case #{}: {}'.format(t + 1, alg(stack)))
