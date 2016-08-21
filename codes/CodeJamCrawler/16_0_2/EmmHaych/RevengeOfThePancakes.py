def main():
    T = int(raw_input())
    
    for t in range(1, T + 1):
        S = raw_input()
        flips = 0
        while True:
            initialSet = getInitialSet(S)
            if(initialSet[1] == '' and initialSet[0][0] == '+'):
                break
            S = flipSet(initialSet[0]) + initialSet[1]
            flips = flips + 1
        print ("Case #" + str(t) + ": " + str(flips))
            
        
def getInitialSet(string):
    setType = string[0]
    if(setType == '-'): setType = '+'
    else: setType = '-'
    initialSet = string.split(setType)[0]
    return (initialSet, string[len(initialSet):])

def flipSet(string):
    result = ''
    for char in string:
        if(char == '-'): result = result + '+'
        else: result = result + '-'
    return result
        
main()