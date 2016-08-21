import sys
import os

In = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[1])
Out = open(os.path.dirname(os.path.abspath(__file__))+'/'+sys.argv[2],'w')
        
if __name__ == '__main__':
    T = int(In.readline())
    for x in range(T):
        print(x)
        N = In.readline().rstrip('\n')
        Seen = set([int(i) for i in N])
        if Seen == {0}:
            Out.write('Case #{}: {}\n'.format(x+1,'INSOMNIA'))
            continue
        N = int(N)
        kN = N
        while not Seen == {0,1,2,3,4,5,6,7,8,9}:
            kN += N
            Seen = Seen.union([int(i) for i in str(kN)])
        Out.write('Case #{}: {}\n'.format(x+1,kN))

 
                

                    
                  
            
