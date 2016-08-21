#!/usr/bin/env python


with open("x") as f:
    array = [x for line in f for x in line.split()]

with open("fw", 'w') as f:
    for test in range(1, len(array)):

        num = array[test]
        f.write("Case #" + str(test) + ": ")
        s = array[test][::-1]
        print s
        matrix = [[None]*2 for i in range(len(s) + 1)]
        matrix[0][0] = 0

        for i in range(len(s)):
            for j in range(2):
                if matrix[i][j] is None:
                    continue
                if (j == 0) != (s[i] == '+'):
                    v = matrix[i + 1][j ^ 1]
                    if v == None or v > matrix[i][j] + 1:
                        v = matrix[i][j] + 1
                    matrix[i + 1][j ^ 1] = v
                else:
                    v = matrix[i + 1][j]
                    if v == None or v > matrix[i][j]:
                        v = matrix[i][j]
                    matrix[i + 1][j] = v
        f.write(str(min([x for x in matrix[len(s)] if x is not None])) + "\n")