#!/bin/python
f = open('test.txt', 'r')
output = open('output.txt', 'w')

c = 0
for line in f:
    if c != 0:
        changes = -1
        prev_char = ' '
        for char in line:
            if char != prev_char and (char=='+' or char== '-'):
                changes += 1
                print('Case #{}:  {} -> {}'.format(c, prev_char, char))
            prev_char = char
        result = changes +1;
        if line[len(line)-2] == '+':
            result -= 1
        output.write('Case #{}: {}\n'.format(c, result))

    c += 1

output.close()
f.close()
