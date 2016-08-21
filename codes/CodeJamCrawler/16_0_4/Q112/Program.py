import sys
import os

In = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[1])
Out = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[2],'w')
        
if __name__ == '__main__':
    T = int(In.readline())
    for x in range(T):
        K,C,S = In.readline().rstrip('\n').split(' ')
        sol = ''
        for i in range(int(K)):
            sol += str(i+1)+' '
        Out.write('Case #{}: {}\n'.format(x+1,sol))

 
                

                    
                  
            
