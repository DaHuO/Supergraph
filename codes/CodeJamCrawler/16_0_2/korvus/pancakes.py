def flip(stack):
    return ['+' if ch=='-' else '-' for ch in stack[::-1]]

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
num_cases = int(raw_input())  # read a line with a single integer
for casenum in xrange(num_cases):
    orientations = raw_input()
    moves = 0
    stack = [ch for ch in orientations]
    while not all((c == '+' for c in stack)):
        #print stack
        numdone = 1
        while stack[-numdone] == "+":
            numdone = numdone+1
        numdone = numdone - 1
        if numdone == 0:
            done = []
            left = stack[:]
        else:
            done = stack[-numdone:]
            left = stack[:-numdone]
        #print "done: "+repr(done)+"  left: "+repr(left)    
        if left[0] == '+':
            num_right = 1
            while stack[num_right] == '+':
                num_right = num_right + 1
            moves = moves + 1
            left = flip(left[:num_right]) + left[num_right:]
        moves = moves + 1
        stack = flip(left) + done
        
        
    print "Case #{}: {}".format(casenum+1, moves)

