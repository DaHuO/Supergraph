

def calculatemin(stack):
    counter = 0
    print('new stack')
    if checktrue(stack):
        return counter
    else:
        for i in xrange(len(stack)-1, -1, -1):
            #print(stack[i])
            print(i, stack[i])
            if stack[i] == '-':
                stack = flippartialstack(stack, i)
                print('im in')
                print(stack)
                counter+=1
                if checktrue(stack):
                    print(counter)
                    return counter

def checktrue(s):
     return (s == len(s) * '+')

def flippartialstack(stack, index):
    if len(stack)>1:
        unchanged = stack[index+1:]
    else:
        unchanged = ""
    #print('unchanged:' + (',').join(unchanged))
    changestack = stack[:index+1]
    #print('change:' + (',').join(changestack))
    changestack = changestack.replace('+', '1')
    changestack = changestack.replace('-', '+')
    changestack = changestack.replace('1', '-')
    #print('new stack:' + (',').join(changestack)+(',').join(unchanged))
    return changestack+unchanged

def outputfile(answers):
    f = open('output.out', 'a')
    for i, v in enumerate(answers):
        f.write('Case #' + str(i+1) + ': ' + str(v) + '\n')
    f.close()
                   
def vapenaesh():
    fname = 'B-large.in'
    content = []
    answers = []
    with open(fname) as o:
        for line in o:
            content.append(line.rstrip())
    content = content[1:]
    for stack in content:
        answers.append(calculatemin(stack))
    outputfile(answers)

vapenaesh()
    
