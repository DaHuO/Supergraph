# Test Cases
test_cases = int(raw_input())

# Input Cake Stack
cake_stacks = []

def process_stack(cake_stack):
    counter = 0
    if len(cake_stack) == 1:
        if cake_stack[0] == "+":
            counter = 0
    for i in range(0, len(cake_stack)-1):
        if cake_stack[i] != cake_stack[i+1]:
            counter += 1
            cake_stack = flip(i, cake_stack)
    if cake_stack[0] == "-":
        counter += 1
        cake_stack = flip(len(cake_stack)-1, cake_stack)
    return counter

def flip(index, cake_stack):
    for i in range(0, index + 1):
        if cake_stack[i] == "-":
            cake_stack[i] = "+"
        else:
            cake_stack[i] = "-"
    return cake_stack

# Take all inputs
for x in range(1, test_cases + 1):
    cake_stacks.append(raw_input())

for natural_cake_stack in cake_stacks:
    cake_stack= list(natural_cake_stack)
    number = process_stack(cake_stack)
    print "Case #%d: %d" %(cake_stacks.index(natural_cake_stack)+1, number)
