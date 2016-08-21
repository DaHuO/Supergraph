import os
import sys


def flip(symbol):
    if symbol == '+':
        return '-'
    else:
        return '+'

def flip_pancakes(stack, flip_end):
    # reverse stack first
    extra_flip = (flip_end + 1) % 2
    for i in range(0,(flip_end+1)/2):
        temp = stack[i]
        stack[i] = stack[flip_end - i]
        stack[flip_end - i] = temp
        # Now flip
        stack[i] = flip(stack[i])
        stack[flip_end - i] = flip(stack[flip_end - i])     
    if extra_flip:
        stack[flip_end/2] = flip(stack[flip_end/2])


def pancake_fliper(stack):
    flips = 0
    stack_end = len(stack) - 1
    while True:
        if '-' not in stack:
            return flips 
        while stack[stack_end] == '+':
            stack_end = stack_end - 1
        # Find point to flip
        flip_end = stack_end
        if stack[0] == '+':
            while stack[flip_end] == '-':
                flip_end = flip_end - 1
        flips = flips + 1
        flip_pancakes(stack, flip_end)

def sheep_sleeps(inp):
    op = open("output.txt","w")
    ip = open(inp)
    file_inp = ip.read().splitlines()
    test_cases = int(file_inp[0])
    for case in range(1,test_cases+1):
        final_number = pancake_fliper(list(file_inp[case]))
        op.write("Case #%s: %s\n" % (case, final_number))
    op.close()
    ip.close()

if __name__ == '__main__':
    sheep_sleeps(sys.argv[1])

