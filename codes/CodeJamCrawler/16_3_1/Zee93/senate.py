# take input
import copy
leterals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
with open('A-large.in') as in_f:
    n = int(in_f.readline()[:-1])
    cases = []
    for i in range(n):
        case = [int(in_f.readline()[:-1]), list(map(int, in_f.readline()[:-1].split(' ')))]
        case = case[1]
        new_case = []
        for i in range(len(case)):
            new_case.append([leterals[i], case[i]])
        cases.append(new_case)


out_f = open('a.out', 'r+')

results = []
i = 0
for current in cases:
    i += 1
    way = []
    while(sum(list(map(lambda a: a[1], current)))):
        current = sorted(current,key=lambda a: a[1], reverse=True)
        possible = copy.deepcopy(current)
        possible[0][1] -= 1
        possible[1][1] -= 1
        can = True
        for j in possible:
            if j[1] > 0.5*sum(list(map(lambda a: a[1], possible))):
                can = False
        if not can:
            current[0][1] -= 1
            way.append(current[0][0])
        else:
            current = possible
            way.append(current[0][0] + current[1][0])


    results.append('Case #{}: '.format(i) + ' '.join(way) + '\n')

out_f.writelines(results)
out_f.close()
