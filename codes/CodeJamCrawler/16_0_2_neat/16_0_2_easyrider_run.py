#!/usr/bin/python
from __future__ import print_function

nr_of_testcases = int(raw_input())



def parse_row(pancakes):
    output = []
    for pancake in pancakes:
        if pancake == "+":
            output.append(True)
        else:
            output.append(False)

    return output

def calc_changes(stack):
    nr_of_changes = 0
    for index in range(1,len(stack)):
        if stack[index] is not stack[index-1]:
            nr_of_changes = nr_of_changes + 1

    return nr_of_changes



def flip_row(pancakes, index):
    pass

for i in range(1,nr_of_testcases+1):
    new_stack = raw_input()
    pancakes = parse_row(new_stack)
    nr_of_flips = calc_changes(pancakes) + int(not pancakes[-1])

    result = nr_of_flips


    print("Case #{task}: {result}".format(task=i,
                                 result=str(result)))
