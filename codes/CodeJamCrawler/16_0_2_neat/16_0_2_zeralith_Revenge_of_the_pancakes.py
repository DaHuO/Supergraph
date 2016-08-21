c_flip = 0
counter = 0
def flip_case(stack):
    while('-' in stack):
        prev = stack[0]
        if prev is '+':
            j = 1
            while stack[j] == '+':
                j += 1
            stack = flip(stack,j)
        else:
            doit = False
            for i in range(1,len(stack)):
                if stack[i-1] is '+' and stack[i] is '-':
                    doit = True
            if doit:
                indx = len(stack)
                for i in range(len(stack)-1,1,-1):
                    if stack[i] is '+':
                        indx -= 1
                    else:
                        break
                stack = flip(stack,indx)
            else:
                indx = 0
                for item in stack:
                    if item is '-':
                        indx += 1
                    else:
                        break
                stack = flip(stack,indx)

        #print(stack)
        #input()

def flip(stack,n):
    global c_flip
    tmp = stack[n-1::-1]
    stack = tmp + stack[n::]
    for indx in range(0,n):
        if stack[indx] is '-':
            stack[indx] = '+'
        else:
            stack[indx] = '-'
    c_flip += 1
    return stack

t = int(input())
stacks_pancakes = []

for x in range(0,t):
    stacks_pancakes.append(input())

for stack in stacks_pancakes:
    counter += 1
    stack = list(stack)
    c_flip = 0
    flip_case(stack)

    print("Case #{}: {}".format(counter,c_flip))