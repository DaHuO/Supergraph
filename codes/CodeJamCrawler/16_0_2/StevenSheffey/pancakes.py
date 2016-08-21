import sys

stacks = [line.rstrip() + '+' for line in sys.stdin.readlines()[1:]]


for case, stack in enumerate(stacks):
    num_moves = 0
    for i in range(1,len(stack)):
        if stack[i] != stack[i-1]:
            num_moves += 1
    print("Case #{}: {}".format(case+1,num_moves))
