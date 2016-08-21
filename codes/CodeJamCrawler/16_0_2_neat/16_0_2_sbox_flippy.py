#!/bin/python

def swap_sign(sign):
    return {
                '-':'+',
                '+':'-'
            }[sign]

def flip(line):
    result = list(reversed(line))
    result = [ swap_sign(pancake) for pancake in result]
    return "".join(result)

def smiling(line):
    for char in line:
        if char == "-":
            return False
    return True

def flippin_ballz(line):
    flip_count = 0
    if len(line) == 1 :
        if line[0] == "-":
            flip_count += 1
            flip(line)
            return flip_count
        else:
            return flip_count 

    while not smiling(line):
        index = 0
        pre_panface = line[0]
        for panface in line:
            if pre_panface == panface:
                index += 1
                pre_panface = panface
            else:
                break
        line = flip(line[:index]) + line[index:]
        flip_count += 1
    return flip_count 

lines = int(input())
for line_num in range(1,lines+1):
    line = input()
    print("Case #{}: {}".format(line_num,flippin_ballz(line)))
