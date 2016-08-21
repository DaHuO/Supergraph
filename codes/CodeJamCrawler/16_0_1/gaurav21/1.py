#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cont_saxena
#
# Created:     08/04/2016
# Copyright:   (c) cont_saxena 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def Solve(N):
    J = 0
    b = str(N)
    stack = [x for x in b]
    stack = list(set(stack))
    #print stack
    if N == 0 :
        return "INSOMNIA"
    else :
        current = 2
        while len(stack) < 10 :
            J  = current*N
            #print J
            b = str(J)
            for a in b:
                if a in stack:
                    pass
                else :
                    stack.append(a)
            #print stack
            current += 1
        return J

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1,T+1):
        N = f.readline()
        num = Solve(int(N))
        print ("Case #"+str(case)+": "+str(num))