
input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = map(int, data.split('\n'))


case = 0
for a_input in input_lines[1:]:
    case += 1
    memory = {}
    digit_mem = {}

    value = -1
    counter = 1
    c_input = a_input

    while c_input not in memory:
        memory[c_input] = True

        temp = c_input
        while temp:
            digit_mem[temp % 10] = True
            temp /= 10

        if len(digit_mem) == 10:
            value = c_input
            break

        counter += 1
        c_input = a_input * counter


    if value == -1:
        value = 'INSOMNIA'

    output_lines.append('Case #%s: %s' % (case, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)