import copy
import numpy as np
import sys
a=open(sys.argv[-1]).readlines()[1:]
problems = []
for i in a[1::2]:
    problems.append([int(j) for j in i.split()])

def solve(problem):
    ans = []

    while sum(problem) != 0:
        max_s = max(problem)
        test = copy.copy(problem)
        test.remove(max_s)
        max_2 = max(test)
        tot_s = sum(problem)
        if max_2 * 2 <= tot_s - 2 and (max_s - 2) * 2 <= tot_s - 2:
            i = problem.index(max_s)
            ans.append([i]*2)
            problem[i] -= 2
        elif max_2 == max_s != 1:
            i1 = -1
            i2 = -1
            for i in range(len(problem)):
                if problem[i] == max_s and i1 == -1:
                    i1 = i
                if problem[i] == max_2 and i1 != i and i1 != -1:
                    i2 = i
                    break
            ans.append([i1, i2])
            problem[i1] -= 1
            problem[i2] -= 1
        elif max_s == 1:
            i1 = -1
            i2 = -1
            if sum(problem) % 2 == 0:
                for i in range(len(problem)):
                    if problem[i] == max_s and i1 == -1:
                        i1 = i
                    if problem[i] == max_2 and i1 != i and i1 != -1:
                        i2 = i
                        break
                ans.append([i1, i2])
                problem[i1] -= 1
                problem[i2] -= 1
            else:
                i = problem.index(max_s)
                ans.append([i])
                problem[i] -= 1
    ansalpha = ''
    for i in ans:
        for j in i:
            ansalpha += chr(j + ord('A'))
        ansalpha += ' '
    return ansalpha


for i in range(len(problems)):
    print 'Case #' + str(i + 1) + ': ' + str(solve(problems[i]))
