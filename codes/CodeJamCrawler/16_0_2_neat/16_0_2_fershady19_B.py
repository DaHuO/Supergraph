f = open('B-large.in.txt', 'r')

cases = f.readline()
    
def AllHappy(stack):
    for pancake in stack:
        if pancake != '+':
            return False
    return True
    
def LastPancake(stack):
    for i in range(1,len(stack)):
        if(stack[i] != stack[0]):
	   return i-1;
    return len(stack) - 1
    
def RevengeOfThePancakes(stack):
    turns = 0
    while (not AllHappy(stack)):
        last = LastPancake(stack)
        for i in range(last+1):
            if (stack[i] == '+'):
                stack[i] = '-'
            else:
                stack[i] = '+'
        turns += 1
        
    return turns


for case in range(int(cases)):
    line = list(f.readline())
    line.pop()
    print 'Case #'+str(case+1)+': ' + str(RevengeOfThePancakes(line))
    
