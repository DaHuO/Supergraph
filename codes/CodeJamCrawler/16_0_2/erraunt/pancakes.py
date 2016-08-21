

t = int(input())

for tc in range(1, t+1):
    result = 0
    stack = input()
    if stack[0] == '+' and '-' in stack:
        result += 1
    stack = stack.strip('+')

    minus_groups = 0
    prev_char = '+'
    for i in range(len(stack)):
        if stack[i] == '-' and prev_char != '-':
            minus_groups += 1
        prev_char = stack[i]

    if minus_groups > 0:
        result += 1 + 2 * (minus_groups - 1)

    print("Case #" + str(tc) + ": " + str(result))

