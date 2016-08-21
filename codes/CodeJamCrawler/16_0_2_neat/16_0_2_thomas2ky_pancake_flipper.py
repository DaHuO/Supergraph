'''
Created on Apr 8, 2016

@author: Thomas
'''

def flip_stack(s):
    '''flip the provided stack/substack of pancakes'''
    rev_s = s[::-1]

    # replace with temporary character
    rev_s = rev_s.replace('+', 't')
    # switch - for +
    rev_s = rev_s.replace('-', '+')
    # switch + for -
    rev_s = rev_s.replace('t', '-')
    flipped_s = rev_s
    
    return flipped_s

def greedy_flip(s, side):
    max_pos = s.find(side)
    sub_stack = s[0:(max_pos)]
    fsub_stack = flip_stack(sub_stack)
    stack = fsub_stack + s[max_pos:]
    return stack
    

def flip_decision(stack, num_flips=0):
    '''decide what to flip, do the flip, and continue until all happy faces'''
    
    if "-" in stack:
        # Not all Happy Face Pancakes
        '''
        if (num_flips == 0) and (stack.count('-') > stack.count('+')):
            stack = flip_stack(stack)
        '''
        if '+' not in stack:
            stack = flip_stack(stack)
                    
        elif (stack[0] == "-"):
            # flip stack
            stack = greedy_flip(stack, '+')
              
        elif (stack[0] == "+"):
            # greedy flip subset
            stack = greedy_flip(stack, '-')

        return flip_decision(stack, num_flips+1)
    
    else:
        return num_flips 
        

if __name__ == '__main__':
    out = {}

    with open("B-large.in", 'rb') as f:
        lines = f.readlines()[1:]
        for idx,line in enumerate(lines):
            line = line.rstrip()
            print line + str("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            num_flips = flip_decision(line)
            out[idx+1] = num_flips


    with open("output.out", 'w') as f:
        f.write("")
        for key, val in out.iteritems():
            line = "Case #" + str(key) + ": " + str(val) + "\n"
            f.write(line)