import sys
import numpy as np


def flip(case):
    i = 0
    flips = 0
    
    if len(case) == 1 and sum(case) == 1:
        return i
    elif len(case) == 1 and sum(case) == 0: 
        return i+1
    
    
    for i in range(len(case)-1):      
            
        if case[i] != case[i+1]:
            for j in range(int(i/2)+1):
                temp = case[j] 
                case[j] = not case[i-j]
                case[i-j] = not temp 
            flips +=1
                
    if sum(case) == 0:
        return flips +1 
    elif sum(case) == len(case):
        return flips 
    
def convert(case):
    case_array = np.empty(len(case), dtype = bool)
    for i in range(len(case)):
        if case[i] == '+':
            case_array[i] = True
        else:
            case_array[i] = False
    
    return case_array

def cases(): 
    answer = open('B-large-answer.in', 'w')
    T = int(raw_input())  
    for i in range(1, T+1):
        case = [s for s in raw_input()]  
        case = convert(case)
        flips = flip(case)
        print >>answer, "Case #{}: {}".format(i, flips)
       
    answer.close()
    
def main():
    cases()
    
if __name__ == '__main__':
    sys.exit(main())