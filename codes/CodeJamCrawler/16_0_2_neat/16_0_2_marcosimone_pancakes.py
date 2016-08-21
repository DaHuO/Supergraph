
inputfile=open('pancakes_input')
input=inputfile.read()
stacks=input.split('\r\n')
stacks.remove(stacks[0])
for index,stack in enumerate(stacks):
    count=0
    stack=stack[::-1]
    while 1:
        if '-' not in stack:
        
            print "Case #%d: %d" % (index+1,count)
            break
        else:
            minus=stack.index('-')
            base=stack[:minus]
            to_flip=stack[minus:]
            to_flip=to_flip.replace("-", "*")
            to_flip=to_flip.replace("+", "-")
            to_flip=to_flip.replace("*", "+")
            stack=base+to_flip
            count+=1