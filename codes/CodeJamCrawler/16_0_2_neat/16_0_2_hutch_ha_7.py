noOfCases = int(raw_input())
output = open("h7_output.txt","w+")
def flip(stk,j):
    new_stk = []
    for i in stk:
        if(i == '+'):
         new_stk.append('-')
        else:
         if (i == '-'):
           new_stk.append('+')
    new_stk.reverse()
    return new_stk

def divide(stk):
    l = len(stk)
    stk2=[]
    val = 1
    for k in stk[::-1]:
        if (k == '+'):
            stk2.append(k)
            val = val +1
        else:
             break
    return stk2,l-val

for i in xrange(1,noOfCases+1):
    moves =0
    stk = raw_input()
    stk = list(stk)
    l = len(stk)
    stk1 = stk
    stk2 = []
    final = []
    if('-' not in stk):
        moves = 0
    else:
        while('-' in stk1):
            stk2, j = divide(stk1)
            stk1 = stk[0:j+1]
            temp=[]
            l = len(stk1)
            val=0
            if(stk1[0]=='+'):
              for k in stk1[::-1]:
                if (k == '-'):
                   temp.append(k)
                   val = val + 1
                else:
                   break
              stk1 = flip(stk[0:l-val], val) + temp
            else:
              stk1 = flip(stk[0:j+1], j)
            stk = stk1
            if(stk2!=[]):
             final.append(stk2)
            else:
                if('-' not in stk1):
                    final.append(stk1)
            moves = moves + 1
    output.write("Case #" + str(i) + ": " +str(moves) + "\n")
