
input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')


def pancake(s, c, state):

    if s == "":
        return c

    target = '+' if state else '-'

    if s[-1] == target:
        c += 1

    return pancake(s[:-1], c, c%2 != 0)



case = 0
for a_input in input_lines[1:]:
    case += 1
    n = len(a_input)

    value = pancake(a_input, 0, False)

    output_lines.append('Case #%s: %s' % (case, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)