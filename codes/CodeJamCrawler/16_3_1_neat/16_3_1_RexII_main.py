


def test(str):
    for i in range(0, len(str)):
        str[i] = str[i]+2

case = int(raw_input())
N = 0



all = 0

for i in range(0, case):
    
    out = "Case #"
    out += str(i+1) + ": "
    
    N = int(raw_input())
    P = raw_input()
    P = P.split()
    
    P_int = [int(j) for j in P]
    
    count = len(P_int)
    all = sum(P_int)
    
    P_P = []
    
    
    idx = 0
    for j in P_int:
        tmp = chr(ord('A')+idx), j
        P_P.append(tmp)
        idx += 1
    
    
    P_P = sorted(P_P, key=lambda x:x[1])
    
    while all > 3:
        
        out += P_P[-1][0]
        P_P[-1] = [P_P[-1][0], P_P[-1][1]-1]
        P_P = sorted(P_P, key=lambda x:x[1])

        out += P_P[-1][0]
        P_P[-1] = [P_P[-1][0], P_P[-1][1]-1]
        P_P = sorted(P_P, key=lambda x:x[1])
            
        out += ' '
        all -= 2
        
    if(all == 3):
        out += P_P[-1][0]
        P_P[-1] = [P_P[-1][0], P_P[-1][1]-1]
        P_P = sorted(P_P, key=lambda x:x[1])
        out += ' '
        all -= 1
    
    if(all == 2):
        out += P_P[-1][0]
        P_P[-1] = [P_P[-1][0], P_P[-1][1]-1]
        P_P = sorted(P_P, key=lambda x:x[1])

        out += P_P[-1][0]
        P_P[-1] = [P_P[-1][0], P_P[-1][1]-1]
        P_P = sorted(P_P, key=lambda x:x[1])
        all -= 2
    
    #print P_P
    
    '''
    idx = 0
    print P
    for j in P:
        if j == '':
            break
        #P_int.append(int(P[idx]))
        print int(j)
        idx += 1
      '''
      
    print out 


    
    
    