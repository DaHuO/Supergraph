import sys

for x in range(1, int(sys.stdin.readline()) + 1):
    stack = list(sys.stdin.readline().strip())
    while stack and stack[-1] == '+':
        stack.pop()
    if stack:
        y = 1
        current = '-'
        for z in reversed(stack):
            if z != current:
                current = z
                y += 1
    else:
        y = 0
    print('Case #{}: {}'.format(x, y))
