def pancakes(stack):
    n = len(stack)
    f = 0
    while stack.count("+") < n:
        if stack[0] == "+":
            for i in range(n):
                if stack[i] == "+":
                    stack[i] = "-"
                else:
                    break
        else:
            for i in range(n):
                if stack[i] == "-":
                    stack[i] = "+"
                else:
                    break
        f +=1  
    return f

    
n = int(raw_input())
for i in range(n):
    stack = raw_input()
    count = pancakes(list(stack))
    print "Case #{0}: {1}".format(i+1, count)
    
