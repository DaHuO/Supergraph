# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 01:52:15 2016

@author: jsevillamol
"""

from collections import deque

def solve_case(stack):
    return BFSearch(stack)
    
def BFSearch(stack):
    if solution(stack):
        return 0
    
    frontier = deque()
    frontier.append(stack)
    explored = set()
    cost = 0
    while frontier:
        new_frontier = deque()
        cost +=1
        while frontier:
            stack = frontier.popleft()
            explored.add(stack)
            for move in possible_movements(stack):
                if not move in explored:
                    if solution(move): return cost
                    new_frontier.append(move)
        frontier = new_frontier

def possible_movements(stack):
    moves = []
    aux = stack.rstrip('+')
    for i in range(1, len(aux)+1):
        new_stack = reverse(stack[0:i])+stack[i:]
        moves.append(new_stack)
    return moves

def reverse(stack):
    l = ['+' if x=='-' else '-' for x in stack]
    l.reverse()
    return "".join(l)

def solution(stack):
    for i in stack:
        if i == '-': 
            return False
    return True


if True:
    with open("out.txt", 'w') as out:
        with open("in.data") as file:
            n = int(file.readline())
            for i in range(n):
                sol = solve_case(file.readline())
                out.write("Case #{}: {}\n".format(i+1,sol))