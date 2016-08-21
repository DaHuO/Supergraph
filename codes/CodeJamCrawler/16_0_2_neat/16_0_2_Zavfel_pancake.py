t = int(raw_input())  # read a line with a single integer

def flip(state, n):
    num = len(state)
    
    result = ''
    for i in xrange(n,-1,-1):
        if state[i] == '-':
            result += '+'
        else:
            result += '-'

    result += state[n+1:]
    return result

def notHappy(state):
    for i in state:
        if i=='-':
            return True
    return False




for i in xrange(1, t + 1):
    state =  raw_input()
    count = 0
    length = len(state)
    if (length==1):
        if state[0]=='-':
            print "Case #" + str(i) + ": 1"
        else:
            print "Case #" + str(i) + ": 0"
        continue

    while (notHappy(state)):
        count+=1
        isPos = False        
        if state[0]=='+':
            isPos = True
        for j in xrange(1,length):
            if isPos:
                if state[j]=='-':
                    state = flip(state,j-1)
                    break
            else:
                if state[j]=='+':
                    state = flip(state,j-1)
                    break
            if j==length-1:
                state = flip(state,j)
                
    print "Case #" + str(i) + ": " + str(count)
    
