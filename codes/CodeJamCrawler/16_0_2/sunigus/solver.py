# -*- codigng: utf-8 -*-

input_data = ['-', '-+', '+-', '+++', '--+-']

input_data = []
with open('problemB\B-large.in') as f:
    for (i, line) in enumerate(f):
        if i < 1:
            continue
        else:
            input_data.append(line[:-1])

output_data = []
for ss in input_data:
    state = ss[0]
    cnt = 0
    for s in ss:
        if s != state:
            cnt += 1
            state = s
    else:
        if state == '-':
            cnt += 1
    output_data.append(cnt)

print(input_data)
print(output_data)

with open('problemB\output_large.txt', 'w') as f:
    for (i, output) in enumerate(output_data):
        f.write('Case #{0}: {1}\n'.format(i + 1, output))
