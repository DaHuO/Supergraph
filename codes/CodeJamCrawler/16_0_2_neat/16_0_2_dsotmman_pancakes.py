#!/usr/bin/env python

from __future__ import print_function

def all_face_up(stack):
    return True if stack.count('-') == 0 else False

def flip_first_i(stack, i):
    def flip(face):
        return '+' if face == '-' else '-'
    return "".join([ flip(j) for j in stack[:i] ]) + stack[i:]

def soln(stack):
    # algorithm: we look for the bottom most pancake
    # that is face down (index i) and we flip the first
    # i pancakes. repeat until all are face up
    i = 0
    while not all_face_up(stack):
        # don't need to check return value, index
        index = stack.rfind('-') + 1
        stack = flip_first_i(stack, index)
        i += 1
    return i

if __name__=='__main__':
    T = int(raw_input())
    for i in range(T):
        print("CASE #{}: {}".format(i+1, soln(raw_input())))
