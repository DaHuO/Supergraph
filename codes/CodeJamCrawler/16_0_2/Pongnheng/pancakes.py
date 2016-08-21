#!/usr/bin/python

def flip(i, stack):
    sub = stack[:i]
    if sub[0] == '-': return ('+' * i) + stack[i:] 
    else: return ('-' * i) + stack[i:] 

def all_same_face(stack):
    top = stack[0]
    for i in xrange(1, len(stack)):
        if top != stack[i]:
            return False
    return True

def all_happy_face(stack):
    return all_same_face(stack) and stack[0] == '+'

def all_unhappy_face(stack):
    return all_same_face(stack) and stack[0] == '-'

def convert(stack, count):
    if all_happy_face(stack): return count
    elif all_unhappy_face(stack): return count + 1
    else:
        i = 1
        top = stack[0]
        while top == stack[i]:
            i = i + 1
        stack = flip(i, stack)
        return convert(stack, count + 1)


t = int(raw_input())
for i in xrange(1, t + 1):
    stack = raw_input()
    result = convert(stack, 0)
    print "Case #{}: {}".format(i, result)

