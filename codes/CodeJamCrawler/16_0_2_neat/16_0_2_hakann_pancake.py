def reduce_stack(panstack):
    panstack = panstack.rstrip('+')
    if panstack == '':
        return 0
    panlist = list(panstack)
    reduced_stack = [panlist[0]]
    for pancake in panlist[1:]:
        if reduced_stack[-1] != pancake:
            reduced_stack.append(pancake)
    return len(reduced_stack)
        
def formatted_output(index, result):
    return 'Case #' + str(index) + ': ' + str(result)


t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    n = str(raw_input())  # read a list of integers, 2 in this case
    print formatted_output(i, reduce_stack(n))
    # check out .format's specification for more formatting options