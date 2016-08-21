def happy(inpt):
    case = 0
    for line in inpt:
        if not case:
            case += 1
            continue
        else:
            stack = line[:-1]
            count = 1
            for index in range(len(stack)-1):
                if stack[index] != stack[index + 1]:
                    count += 1
            if stack[-1] == '+':
                count -= 1
            print('Case #' + str(case) + ': ' + str(count))
            case += 1
