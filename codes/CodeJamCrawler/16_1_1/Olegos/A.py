def solve(string):
    if string[-1] == '\n':
        string = string[:-1]
    result = string[0]
    for l in string[1:]:
        if l < result[0]:
            result = result + l
        else:
            result = l + result
    return result

input_file = open('in.txt', 'r')
strings = []
for line in input_file:
    strings.append(line)


output_file = open('out.txt', 'w')
case = 1
for s in strings[1:-1]:
    output_file.write('Case #{}: {}\n'.format(case, solve(s)))
    case += 1
output_file.write('Case #{}: {}'.format(case, solve(strings[-1])))