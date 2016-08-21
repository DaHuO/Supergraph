'''
Created on Apr 9, 2016

@author: kevin
'''



import sys

def opposite(input):
    if (input == '+'):
        return '-'
    else:
        return '+'
    
def pancake_flip(input):
    
    if (len(input) < 1):
        return 0
    
    flips = 0
    while True:
        first_panckae = input[0]
        first_opposite_pancake = input.find(opposite(first_panckae))
        # Find first opposite pancake and flip from there
        if (first_opposite_pancake > 0):
            new_pancake_stack = ""
            for j in range(first_opposite_pancake):            
                new_pancake_stack += opposite(input[j]) 
            flips  = flips  + 1
                
            input = new_pancake_stack + input[first_opposite_pancake:]
            
        pancake_set = set([v for v in input])
        
        if len(pancake_set) == 1:
            if (pancake_set.pop() == '+'):
                return flips
            else:
                return flips + 1
           
if __name__ == '__main__':
    num_cases = int(sys.argv[1])
    
    for i in range(num_cases):
        value = sys.argv[i+2]
        print "Case #%s: %s" % (i + 1, pancake_flip(value))