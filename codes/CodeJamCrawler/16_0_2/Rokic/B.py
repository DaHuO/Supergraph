
def flip(l):
    stack = l.copy()
    if '-' not in stack:
        return 0
    while stack[-1]=='+':
        stack.pop()
    key = stack[0]
    count = 1
    for pancake in stack:
        if pancake!=key:
            key = pancake
            count += 1
    return count

with open('B-large.in') as input_file:
    with open('B-large.out', 'w') as output_file:
        T = int(input_file.readline())
        
        for t in range(1, T+1):
            l = list(input_file.readline().strip())
            
            if t!=T:
                output_file.write('Case #{}: {}\n'.format(t, flip(l)))
            else:
                output_file.write('Case #{}: {}'.format(t, flip(l)))