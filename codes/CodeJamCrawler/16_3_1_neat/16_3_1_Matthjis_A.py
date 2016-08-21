import numpy as np
import sys



def plan(N, P):
    answer = ''
    while sum(P) > 0:        
        max1 = max(P) 

        max_index = P.index(max(P))
        P[max_index] -= 1
        answer += ' ' 
        answer += chr(max_index + ord('A'))
        
        max_index2 = P.index(max(P))
        P[max_index2] -= 1
        if max(P) > sum(P)/2.:
            P[max_index2] += 1
        else:
            answer += chr(max_index2 + ord('A'))

            
            
        
    return answer

def main():
    fout = open('answer_A_small.txt', 'w')
    T = int(raw_input())
    for t in range(1,T+1,1):
        P = []
        N = int(raw_input())
        P = [int(a) for a in raw_input().split(' ')]

        np.array(P)
        answer = plan(N,P)
        
        print>>fout, "Case #{}:{}".format(t, answer)
    
    fout.close()
    
if __name__ == '__main__':
    sys.exit(main())

