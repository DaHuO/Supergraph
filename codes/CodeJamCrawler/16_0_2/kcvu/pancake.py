#!/usr/bin/env python

def count_side_changes(pancake_stack):
    return sum([1 for i in range(1,len(pancake_stack)) if pancake_stack[i-1] != pancake_stack[i]])

def num_of_flips(pancake_stack):
    result = count_side_changes(pancake_stack)
    if pancake_stack[-1] == '-':
        return result + 1
    return result

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as infile:
        _ = infile.readline()
        line_index = 0
        for line in infile:
            pancake_stack = line.strip()
            line_index += 1
            print 'Case #%d: %d' % (line_index,num_of_flips(pancake_stack))

