
# coding: utf-8

# In[17]:

def flip(stack, i=None):
    """flip pancakes i-deep"""
    if i is None:
        i = len(stack)
    return [not x for x in reversed(stack[:i])] + stack[i:]


# In[18]:

def prune(stack):
    while stack and stack[-1]:
        stack.pop()
    return stack


# In[22]:

def solve(stack):
    prune(stack)
    if not stack: # done
        return 0
    if not any(stack): # flip the whole stack
        return 1
    if stack[0]:
        stack = flip(stack, stack.index(False))
        return solve(stack) + 1
    else:
        stack = flip(stack)
        return solve(stack) + 1
    


# In[28]:

cases = int(input())
for case in range(1, 1+cases):
    stack = [pancake == "+" for pancake in input()]
    solution = solve(stack)
    print("Case #{}: {}".format(case, solution))


# In[ ]:



