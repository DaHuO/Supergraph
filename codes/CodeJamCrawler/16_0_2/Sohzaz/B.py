#!/usr/bin/python3


import sys

def flip(arr, pos):
    temp = arr[pos::-1]
    for j, t in enumerate(temp):
        if t == '-':
            arr[j] = '+'
        elif t == '+':
            arr[j] = '-'
    return arr





lines = []



with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.strip())

lines.pop(0)
for index, l in enumerate(lines, start=1):
    arr = list(l)
    if not '+' in arr:
        print("Case #" + str(index) + ": 1")
    elif not '-' in arr:
        print("Case #" + str(index) + ": 0")
    else:
        mov = 0
        while '-' in arr:
            done = False
            i = 0
            if not '+' in arr:
                print("Case #" + str(index) + ": " + str(mov + 1))
                done = True
                break
            while i < (len(arr) - 1):
                if arr[i] != arr[i + 1]:
                    arr = flip(arr, i)
                    mov += 1
                    break
                i += 1

        if not done:
            print("Case #" + str(index) + ": " + str(mov))

