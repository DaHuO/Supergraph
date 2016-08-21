File=open("B-large.txt",'w')
def flip(stack,end):
    top_stack=stack[:end+1]
    bottom_stack=stack[end+1:]
    flip_stack=[]
    for p in range(len(top_stack)):
        if top_stack[p]=='+':
            flip_stack.append('-')
        elif top_stack[p]=='-':
            flip_stack.append('+')
    flip_stack.reverse()
    flip_stack.extend(bottom_stack)
    return flip_stack
            
T=int(raw_input())
for t in range(T):
    S=list(raw_input())
    Srev=S[:]
    Srev.reverse()
    y=0
    while not S.count('+')==len(S):
        for s in Srev:
            if not s=='+':
                n=len(Srev)-(Srev.index(s)+1)
                break
        if S[0]=='-':
            S=flip(S,n)
            y=y+1
            Srev=S[:]
            Srev.reverse()
        else:
            for s in S:
                if not s=='+':
                    S=flip(S,S.index(s)-1)
                    y=y+1
                
                    S=flip(S,n)
                    y=y+1
                    Srev=S[:]
                    Srev.reverse()
                    break
    print >> File, "Case #%d: %d" %(t+1,y)
File.close()
