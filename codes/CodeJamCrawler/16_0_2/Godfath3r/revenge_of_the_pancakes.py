def flip_pancakes(pancakes, i):
    temp = ''
    for pancake in pancakes[:i]:
        if pancake == '-':
            temp += '+'
        if pancake == '+':
            temp += '-'
    flipped = temp[::-1] + pancakes[i:]
    return flipped

def all_downside(stack):
    for pancake in stack:
        if pancake == '+':
            return False
    return True

def flipping(stack):
    flips = 0
    while '-' in stack:
        prev = stack[0]
        for i in range(1, len(stack)):
            if stack[i] != prev:
                stack = flip_pancakes(stack, i)
                flips += 1
            prev = stack[i]
        if all_downside(stack):
            stack = flip_pancakes(stack, len(stack))
            flips += 1
    return flips

i = 1
for test in range(int(raw_input().strip())):
    stack = str(raw_input().strip())
    print 'Case #{}: {}'.format(i, flipping(stack))
    i += 1