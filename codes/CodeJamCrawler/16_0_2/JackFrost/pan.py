T = int(input())

def FLIP(STACK):
    STACK.reverse()
    #print STACK
    F = 0
    while True:
        if STACK[-1] != "+":
            break
        F = 1
        del STACK[-1]
    
    STACKZ = []
    for a in STACK:
        if a == "-":
            STACKZ.append("+")
        else:
            STACKZ.append("-")
    F += 1
    return STACKZ, F

for a in range(1,T+1):
    STACK = list(raw_input())
    F = 0
    while True:
#        print STACK
        if STACK[-1] == "+":
            del STACK[-1]
        #FLIP
        else:
            STACK, A = FLIP(STACK)       
            F += A
        if not STACK:
            print "Case #" + str(a) + ": " + str(F)
            break
