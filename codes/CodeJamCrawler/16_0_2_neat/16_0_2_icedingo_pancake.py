T = int(input())

for t in range(1, T+1):
    stack = input()

    print('Case #{}: '.format(t), end='')

    flips = 0
    current = stack[0]

    for c in stack:
        if c != current:
            flips += 1
            current = c

    if current == '-':
        flips += 1
    

    print(flips)


