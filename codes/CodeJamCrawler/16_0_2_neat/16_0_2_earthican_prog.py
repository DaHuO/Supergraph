'''
Google Code Jam 2016
Problem B. Revenge of the Pancakes
by Justin Cano
'''
from Queue import Queue

def flip(stack, i):
    top = upside_down(stack[:i])
    return top + stack[i:]

def upside_down(stack):
    new_stack = []
    for p in stack:
        if p == '-':
            new_stack.append('+')
        else:
            new_stack.append('-')
    return ''.join(new_stack[::-1])

def is_happy(stack):
    return all(map(lambda p: p == '+', stack))

class Node(object):
    def __init__(self, stack, level=0):
        self.stack = stack
        self.level = level


def solve(stack):
    q = Queue()
    visited = set()
    q.put(Node(stack))
    while not q.empty():
        currnode = q.get()
        if currnode.stack in visited:
            continue
        visited.add(currnode.stack)

        if is_happy(currnode.stack):
            return currnode.level

        for i, p in enumerate(currnode.stack):
            new_pancakes = flip(currnode.stack, i+1)
            q.put(Node(new_pancakes, currnode.level+1))

    return None

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(1, T+1):
        stack = raw_input()
        print 'Case #%d:' % i, solve(stack)