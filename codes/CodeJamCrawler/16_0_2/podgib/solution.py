input = open('B-large.in', 'r')
output = open('B-large.out', 'w')

tokens = input.readline().split(' ')

T = int(tokens[0])

for X in range(1,T+1):
    swaps = 0
    state = ''
    stack = input.readline().strip()

    for c in stack:
        if c == state:
            continue
        state = c
        swaps += 1
    if state == '+':
        swaps -= 1

    print "Case #" + str(X) + ": " + str(swaps)
    output.write("Case #" + str(X) + ": " + str(swaps) + "\n")
