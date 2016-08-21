# -*- coding: utf-8 -*-

# input_data = [0, 1, 2, 11, 1692]
input_data = []

with open('problemA\A-large.in') as f:
    for (i, line) in enumerate(f):
        if i < 1:
            continue
        else:
            input_data.append(int(line))

output_data = []
for n in input_data:
    digits = set([])
    for i in range(1, 10**6+1):
        digits |= set(str(i * n))
        if len(digits) == 10:
            output_data.append(i * n)
            break
    else:
        output_data.append('INSOMNIA')

print(output_data)

with open('problemA\output_large.txt', 'w') as f:
    for (i, output) in enumerate(output_data):
        f.write('Case #{0}: {1}\n'.format(i + 1, output))
