#!/bin/python

f = open('A-large', 'r')

lines = int(f.readline())
print lines

done = []

t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0
for l in range(lines):
    count = count + 1
    case = 'Case #%d: ' % (count)
    # Code
    amount = f.readline()
    teams = map(int,f.readline().split(' '))

    plan = ""

    while sum(teams) > 0:
        p = ""

        m = max(teams)
        i = teams.index(m)
        p += (t[i])
        teams[i] -= 1

        m2 = max(teams)
        i2 = teams.index(m2)
        p += (t[i2])
        teams[i2] -= 1


        if (sum(teams) / 2 < max(teams)):
            teams[i2] += 1
            plan += p[0] + ' '
        else:
            plan += p + ' '

    case += plan[:-1]
    done.append(case)



# Write to file
with open('output.txt', 'w') as f:
    f.write('\n'.join(done))
