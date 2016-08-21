import sys
import os

In = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[1])
Out = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[2],'w')
        
if __name__ == '__main__':
    T = int(In.readline())
    for x in range(T):
        print(x)
        S = In.readline().rstrip('\n')
        Slight = [S[0]]
        sign = S[0]
        for i in range(1,len(S)):
            if S[i] == sign:
                continue
            else:
                Slight.append(S[i])
                sign = S[i]
        if Slight[-1] == '+':
            out = len(Slight)-1
        else:
            out = len(Slight)
        Out.write('Case #{}: {}\n'.format(x+1,out))

 
                

                    
                  
            
