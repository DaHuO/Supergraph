opp = {'-': '+', '+': '-'}

tests = int(input())
t_stacks = []
for t in range(tests):
    t_stacks.append((t, list(input())))
for t_stack in t_stacks:
    t, stack = t_stack
    flips = 0
    while '-' in stack:
        p_stack = stack
        if (stack[0] == '+' and stack[-1] == '-'):
            i = len(stack) - 1
            while stack[i] != '-':
                i -= 1
            while stack[i] != '+':
                i -= 1
            stack = [opp[x] for x in p_stack[:i+1]][::-1] + p_stack[i+1:]
        elif (stack[0] == '+' and stack[-1] == '+'):
            i = len(stack) - 1
            while stack[i] != '-':
                i -= 1
            while stack[i] != '+':
                i -= 1
            stack = [opp[x] for x in p_stack[:i+1]][::-1] + p_stack[i+1:]
        elif (stack[0] == '-' and stack[-1] == '-'):
            stack = [opp[x] for x in p_stack[::-1]]
        else:
            i = len(stack) - 1
            while stack[i] != '+':
                i -= 1
            while stack[i] != '-':
                i -= 1
            stack = [opp[x] for x in p_stack[:i+1]][::-1] + p_stack[i+1:]
        flips += 1
    print('Case #{}: {}'.format(t + 1, flips))
