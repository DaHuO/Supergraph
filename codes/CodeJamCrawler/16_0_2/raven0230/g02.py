T = eval(input())
for i in range(1,1+T):
    stack = input()
    count = 0
    while (set(stack)!={'+'}):
        if (stack[0] == '+'):
            stack = stack.replace('+','-',stack.find('-'))
        elif (set(stack) == {'-'}):
              count += 1
              break
        else:
            stack = stack.replace('-','+',stack.find('+'))
        count+=1
    print("Case #{0}: {1}".format(i,count))
    
