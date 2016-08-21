def getMovements(case, stack):
    stack = list(stack.strip())
    movements = 0
    while('-' in stack):
        index = 0
        for i in range(len(stack)-1,-1,-1):
            if(stack[i] is '-'):
                index = i
                break

        for i in range(0,index+1):
            if(stack[i] is '-'):
                stack[i] = '+'
            else:
                stack[i] = '-'
        movements += 1
    print('Case #'+ str(case)+ ': '+ str(movements))

with open('revenge-pancakes-input.txt', 'r') as f:
    next(f)
    case = 1;
    for line in f:
        getMovements(case,line)
        case+=1
