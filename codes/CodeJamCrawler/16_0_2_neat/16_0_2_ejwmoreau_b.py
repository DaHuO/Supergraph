import fileinput as fi

def flip_pancake(c):
    if c is "-":
        return "+"
    else:
        return "-"

def flip_pancakes(stack, end):
    new_stack = ""
    for c in stack[0:end]:
        new_stack += flip_pancake(c)
    new_stack += stack[end:]
    #print(new_stack)
    return new_stack

def count_continuous(stack):
    end = 1
    char = stack[0]
    for i in range(1, len(stack)):
        if char != stack[i]:
            break
        end += 1
    return end

curr_case = 0
for stack in fi.input():
    if curr_case == 0:
        curr_case += 1
        continue

    rounds = 0
    stack = stack.strip()
    solution = '+' * len(stack)

    while stack != solution and rounds < 10:
        #stack = solution
        count = count_continuous(stack)
        stack = flip_pancakes(stack, count)
        rounds += 1

    print("Case #%s: %s" % (curr_case, rounds))
    curr_case += 1
