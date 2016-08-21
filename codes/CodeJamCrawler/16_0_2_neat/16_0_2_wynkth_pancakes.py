#!/usr/local/bin/python

in_file = open("B-large.in.txt", 'r').readlines()
out_file = open("out.txt", 'wb')


def process_stack(stack):
    while stack[-1]:
        stack = stack[:-1]

    if stack[0]:
        i = 1
        while i < len(stack) and stack[i]:
            i += 1
        for x in range(i):
            stack[x] = False
    else:
        i = 1
        while i < len(stack) and not stack[i]:
            i += 1
        stack = stack[i:]
        old_stack = list()
        for i in range(len(stack)):
            old_stack.append(not stack[-(i + 1)])
        stack = old_stack
    return stack


for case, x in enumerate(in_file):
    if case != 0:
        moves = 0
        stack = map(lambda x: True if x == '+' else False, list(x.replace('\n','')))

        while False in stack:
            stack = process_stack(stack)
            moves += 1

        out_file.write('Case #' + str(case) + ': ' + str(moves) + '\n')


out_file.close()
