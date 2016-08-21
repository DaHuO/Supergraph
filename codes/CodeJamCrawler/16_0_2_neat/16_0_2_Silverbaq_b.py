#!/bin/python

f = open('B-large.in', 'r')

lines = int(f.readline())

lines2 = [word.strip() for word in f]

print lines

done = []

count = 0
for line in lines2:
    count = count + 1
    case = 'Case #%d: ' % (count)
    # Code
    flips = 0

    for i in range(len(line)):
        if i < len(line)-1:
            if line[i] != line[i+1]:
                flips = flips +1

        else:
            if line[i] == '-':
                flips = flips +1
    case += str(flips)
    done.append(case)




# Write to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(done))
