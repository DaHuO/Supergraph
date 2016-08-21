def flip(stack, i):
    for j in range(0, i+1):

        if stack[j] == "-":
            stack[j] = "+"

        elif stack[j] == "+":
            stack[j] = "-"
    return stack


tc = int(raw_input())
for x in range(tc):
    stack = raw_input()
    ans = 0
    stack = list(stack)
    if "-" not in stack:
        print "Case #"+str(x+1)+":",ans
    elif "+" not in stack:
        print "Case #"+str(x+1)+":",ans+1
    else:
            for i in range(0,len(stack)-1):
                if stack[i]!=stack[i+1]:
                    stack = flip(stack, i)
                    ans = ans+1
            if "+" not in stack:
                print "Case #"+str(x+1)+":",ans+1
            else:
                print "Case #"+str(x+1)+":",ans
