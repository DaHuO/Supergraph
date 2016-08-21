f = open("B-large.in", "r")
output = open("B-large.out", "w")

T = int(f.readline().strip())

for idx in range(T):
    i = idx + 1

    origStack = f.readline().strip()
    #print(origStack)
    #Summarize string. Make long strings of + or - just a single char
    oldc = origStack[0]
    stack = [oldc]
    #print("orig stack: ", stack)
    for c in origStack:
    #    print(c)
        if c == oldc:
    #        print("a")
            pass
        else:
    #        print("b")
            oldc = c
            stack.append(c)
    #print()
    #print(stack)
    #We can remove last char if it is '+'
    if stack[-1] == '+':
        stack.pop()
    #    print(stack)


    output.write("Case #%d: %d\n"%(i, len(stack)))
    print("Case #%d: %d"%(i, len(stack)))
    #print("\n")

       
f.close()
output.close()
        
    
