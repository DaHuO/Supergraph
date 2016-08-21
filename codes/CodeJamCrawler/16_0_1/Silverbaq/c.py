#!/bin/python

f = open('A-large.in', 'r')

lines = int(f.readline())
print lines

done = []

count = 0
for N in f:
    count = count + 1
    case = 'Case #%d: ' % (count)
    # Code
    nums = []
    sleeping = False
    i = 1

    while not sleeping:
        name = int(N) * i
        if name < 1:
            case += 'INSOMNIA'
            done.append(case)
            sleeping = True

        for c in str(name):
            if c not in nums:
                nums.append(c)

        i = i +1
        if len(nums) == 10:
            sleeping = True
            case += str(name)
            done.append(case)


# Write to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(done))
