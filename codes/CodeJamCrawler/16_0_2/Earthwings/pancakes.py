'''
Created on 09.04.2016

@author: Dennis Nienhüser <nienhueser@kde.org>
'''

import argparse

def flip(stack, index):
    rev = ''.join(reversed(stack[0:index:]))
    rev = rev.replace('-', 'o')
    rev = rev.replace('+', '-')
    rev = rev.replace('o', '+')
    return rev + stack[index:]

def flips(stack):
    count = 0
    while '-' in stack:
        l = -1
        for i in range(len(stack)):
            if stack[i] == '-':
                break
            assert(stack[i] == '+')
            l = i
        if l >= 0:
            stack = flip(stack, l+1)
            count += 1
        
        r = stack.rfind('-')
        if r >= 0:
            stack = flip(stack, r+1)
            count += 1
    return count

def parse(filename):
    with open(filename) as file:
        numbers = file.readlines()
    return numbers[1:] if len(numbers) > 0 else []

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Code Jam 2016 Q1: Counting Sheep')
    parser.add_argument('file', help='Input text file')
    args = parser.parse_args()
    
    stacks = parse(args.file)
    for index, stack in enumerate(stacks):
        print('Case #{}: {}'.format(index+1, flips(stack)))
    