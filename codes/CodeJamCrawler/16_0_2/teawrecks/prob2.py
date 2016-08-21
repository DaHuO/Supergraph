# Remove consecutive duplicates. Reverse the stack.
from itertools import groupby

t=int(input())
stacks=[input() for i in range(t)]

for i,stack in enumerate(stacks):
    stack = [x[0] for x in groupby(stack)]
    n = (0 if stack[-1] == '+' else 1) + len(stack) - 1
    print("Case #%d: %d"%(i+1,n))