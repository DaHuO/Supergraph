def sol_print(value):
    sol_print.line_number += 1;
    print "Case #%d: %s"%(sol_print.line_number, value)

sol_print.line_number = 0

T = int(raw_input())

inputs = []
for i in range(T):
    inputs.append(raw_input())

for stack in inputs:
    idx = 0
    operation = 0

    while '-' in stack:
        countminus = 0
        if stack[idx] == '+':
            while idx < len(stack) and stack[idx] == '+':
                idx += 1
            while idx < len(stack) and stack[idx] == '-':
                idx += 1
                countminus += 1
            stack = stack.replace('-', '+', countminus)
            operation += 2
        else:
            while idx < len(stack) and stack[idx] == '-':
                idx += 1
                countminus += 1
            while idx < len(stack) and stack[idx] == '+':
                idx += 1
            stack = stack.replace('-', '+', countminus)
            operation += 1
        idx = 0
    sol_print(operation)
