import sys

def good_pancake(pancake):
    return pancake == '+'
    
def flip_pancake(pancake):
    if pancake == '+':
        return '-'
    else:
        return '+'

def test_stack(stack):
    for pancake in stack:
        if not good_pancake(pancake):
            return False
    return True

def flip_stack(stack):
    stack.reverse() 
    for pancake_idx in range(0,len(stack)):
        stack[pancake_idx] = flip_pancake(stack[pancake_idx])
    
    return stack

def group_good(stack):
    idx = 0
    for pancake in stack:
        if not good_pancake(pancake):
            return idx
        else:
            idx = idx + 1
    return idx

def Solve(case):
    flips = 0
    pancakes = list(case)
    if pancakes[-1] != '+' and pancakes[-1] != '-':
        pancakes.pop()
    stack = pancakes[0:len(pancakes)]
    
    while True:
        if  test_stack(pancakes) == True:
            return str(flips)
        
        if good_pancake(stack[-1]):
            stack = stack[0:-1]
            continue
        else:
            if len(stack) == 1:
                if test_stack(stack):
                    continue
                else:
                    pancakes[0:len(stack)+1] = flip_stack(stack)
                    flips = flips + 1
                    continue
            
        idx = group_good(stack)
        if idx > 0:
            stack[0:idx] = flip_stack(stack[0:idx])
            flips = flips + 1
    
        stack = flip_stack(stack)
        flips = flips + 1
        
        pancakes[0:len(stack)] = stack


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "No input file given. Exiting..."
        sys.exit()    
    
    with open(sys.argv[1], 'r') as inputFile:        
        numCases = int(inputFile.readline())

        if numCases <= 0:
            print "No cases"
            sys.exit()
    
        with open('output', 'w') as outputFile:
                
            for i in range(0, numCases):
                case = inputFile.readline()
                print "Input: ", case
                case.split()
                output = Solve(case)
                print "Output: ", output
                outputFile.writelines(["Case #", str(i+1), ": ", output, "\n"])