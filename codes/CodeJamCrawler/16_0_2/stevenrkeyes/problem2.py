
import Queue

def is_happy(stack):
    return set(stack) == set('+')

def get_flipped_stack(stack, i):
    return invert_each_item(stack[0:i][::-1]) + stack[i:]

def invert_each_item(stack):
    return stack.replace("+","5").replace("-","+").replace("5","-")

def get_min_stack_flips(stack):
    # BFS
    q = Queue.Queue()
    # with some memoization in terms of ignoring cycles
    seen_stacks = dict()
    seen_stacks[stack] = True
    # (current stack, num_flips)
    q.put((stack, 0))
    while(True):
        (current_stack, num_flips) = q.get()
        if is_happy(current_stack):
            return num_flips
        practical_flips = range(1,len(current_stack)+1)
        possible_next_flips = [get_flipped_stack(current_stack, i) for i in practical_flips]
        for s in possible_next_flips:
            if not seen_stacks.has_key(s):
                q.put((s, num_flips + 1))
                seen_stacks[s] = True
'''
for size in range(11):
    for stack in [str(bin(i))[2:].zfill(size).replace("1","+").replace("0","-") for i in range(2**size)]:
        print stack, get_min_stack_flips(stack)
'''

import sys
filename = sys.argv[1]
f = open(filename)
lines = f.readlines()

i = 1
for line in lines[1:]:
    print "Case #" + str(i) + ": " + str(get_min_stack_flips(line.replace("\n","")))
    i += 1
