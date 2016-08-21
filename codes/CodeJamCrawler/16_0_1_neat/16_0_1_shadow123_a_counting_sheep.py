'''
Created on Apr 9, 2016

@author: kevin
'''


import sys


def get_case(value):
    number = 0
    if value == value * 2:
        return None
    
    digit_set = set()
    while True:
        number += value
        
        digit_set = digit_set.union(set (v for v in str(number)))
        
        if (len(digit_set)) == 10:
            return number
        
        if number > (sys.maxint - number):
            return None
        
    return None
    
if __name__ == '__main__':
    num_values = int(sys.argv[1])
    for i in range(num_values):
        input_value = int(sys.argv[i + 2])
        solution = get_case(input_value)
        if not solution:
            solution = "INSOMNIA"
        print 'Case #%s: %s' % (i + 1, solution)
        