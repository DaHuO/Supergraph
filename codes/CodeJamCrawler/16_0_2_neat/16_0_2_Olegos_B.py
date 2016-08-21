def flip_pancakes(stack):
    if stack[-1] == '\n':
        stack = stack[:-1]
    prev = stack[0]
    count = 0
    for p in stack:
        if p != prev:
            count += 1
        prev = p
    if stack[-1] == '-':
        count += 1
    return count


input_file = open('in.txt', 'r')
lines = []
for line in input_file:
    lines.append(line)

output_file = open('out.txt', 'w')
case = 1
for line in lines[1:]:
    output_file.write('Case #{}: {}\n'.format(case, flip_pancakes(line)))
    case += 1
