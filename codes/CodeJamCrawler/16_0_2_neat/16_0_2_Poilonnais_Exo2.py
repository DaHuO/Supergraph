#!/usr/bin/python3

f = open("test2.in", 'r')
lines = f.readlines()
f.close()

def flip(line, i):
    k = 0
    save = list(line)
    while (k <= i):
        if save[k] == '+':
            save[k] = '-'
        else:
            save[k] = '+'
        k += 1
    res = ''.join(save)
    return res

def verif(line):
    return line.rfind("-") == -1

nb = 0
i = 0
for line in lines:
    if i == 0:
        nb = int(line)
    if i > 0:
        count = 0
        while not verif(line):
            line = flip(line, line.rfind("-"))
            count += 1
        print("Case #{0}: {1}".format(i, count))
    i += 1
