def main():
    T = int(raw_input())
    for case in range(T):
        stack = raw_input()
        moves = 0
        while '-' in stack:
            topChar = stack[0]
            i = 0
            while i < len(stack) and stack[i] == topChar:
                if stack[i] == '-':
                    stack = stack[:i] + '+' + stack[i+1:]
                else:
                    stack = stack[:i] + '-' + stack[i+1:]
                i += 1            
            moves += 1
        print "Case #" + str(case+1) + ": " + str(moves)

main()
