def evacuate(parties):
    result = ''
    while sum(arr) > 0:
        index = parties.index(max(parties))
        parties[index] -= 1
        result += chr(ord('A') + index)
        if sum(arr) == 2:
            result += ' '
            continue
        index = parties.index(max(parties))
        parties[index] -= 1
        result += chr(ord('A') + index) + ' '
    return result


input_file = open('in.txt', 'r')
lines = []
for line in input_file:
    lines.append(line)
T = int(lines[0])

output_file = open('out.txt', 'w')
lines = lines[1:]
count = 1
for i in range(T):
    arr = []
    line = str(lines[count]).split(' ')
    for num in line:
        arr.append(int(num))
    output_file.write('Case #{}: {}\n'.format(i + 1, evacuate(arr)))
    count += 2
