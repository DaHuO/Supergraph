import sys
import re
#import pdb

class RevengeOfPancakes:
    number_of_flips = 0
        
    def __init__(self):
        self.number_of_flips = 0
            
    def solve(self, pancake_stack):
        if (self.has_blank_side_pancake(pancake_stack) == False):
            return self.number_of_flips
        
        self.number_of_flips = self.make_all_sides_happy(pancake_stack)            
        return self.number_of_flips             

    def make_all_sides_happy(self, pancake_stack):
        all_happy = False
        iterations = 0
        
        while (all_happy == False):
            #pdb.set_trace()
            last_empty = pancake_stack.rfind('-')
            
            
            last_empty += 1
            
            flip_stack = pancake_stack[0:last_empty]
            flip_stack = re.sub(r'-', '#', flip_stack)
            flip_stack = re.sub(r"\+", '-', flip_stack)
            flip_stack = re.sub(r'#', '+', flip_stack)
            
            if (last_empty == len(pancake_stack)):
                pancake_stack = flip_stack
            else:                
                pancake_stack = flip_stack + pancake_stack[last_empty : len(pancake_stack)]
            
            iterations += 1
            all_happy = (self.has_blank_side_pancake(pancake_stack) == False)

        return iterations
                            
    def has_blank_side_pancake(self, pancake_stack):        
        return pancake_stack.find('-') >= 0
        
                                    
file = sys.stdin
#file = open('test_input', "r")
counter = 1
line = file.readline()
line = file.readline()
while line:    
    pancake_stack = line.rstrip('\n')    
    revenge_of_pancakes = RevengeOfPancakes()    
    revenge_of_pancakes.solve(pancake_stack)
    
    print "Case #{}: {}".format(counter, revenge_of_pancakes.number_of_flips)
    line = file.readline()    
    counter += 1