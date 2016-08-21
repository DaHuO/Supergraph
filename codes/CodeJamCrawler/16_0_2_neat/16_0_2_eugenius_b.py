# Re-adapted some of the code from this tutorial
# http://www.redblobgames.com/pathfinding/a-star/implementation.html

import sys
import heapq
import numpy

def flip_pancakes(sequence, location):
    def _flipper(sequence):
        for i, c in enumerate(sequence):
            if i < location:
                yield '1' if c == '0' else '0'
            else:
                yield c
    return ''.join(_flipper(sequence))

def is_happy_pancakes(sequence):
    return len(sequence) == sequence.count('1')

def distance_from_goal(sequence):
    return sequence.count('0')

def heuristic_2(sequence):
    return sum(numpy.abs(numpy.diff(map(int, sequence))))

def get_neighbors_func(sequence):
    for i in range(1, len(sequence)+1):
        yield flip_pancakes(sequence, i)

assert flip_pancakes('000', 3) == '111'
assert flip_pancakes('000', 1) == '100'

assert set(list(get_neighbors_func('000'))) == {'111', '110', '100'}
assert set(list(get_neighbors_func('0'))) == {'1'}

assert is_happy_pancakes('111') == True
assert is_happy_pancakes('110') == False
assert is_happy_pancakes('000') == False
assert is_happy_pancakes('010') == False
assert is_happy_pancakes('1') == True
assert is_happy_pancakes('00') == False

assert distance_from_goal('0000') == 4
assert distance_from_goal('1111') == 0
assert distance_from_goal('1010') == 2

assert flip_pancakes('1110001', 2) == '0010001'
assert flip_pancakes('1110001', 1) == '0110001'
assert flip_pancakes('111', 3) == '000'


class PriorityQueue(object):
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


def a_star_search(start, get_neighbors_func, is_goal_func, heuristic):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()

        if is_goal_func(current):
            break
        
        for neighbor in get_neighbors_func(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                frontier.put(neighbor, priority)
                came_from[neighbor] = current
    return came_from, cost_so_far


def find_cost(pancake_sequence):
    sequence = pancake_sequence.replace('-', '0').replace('+', '1')
    heuristic = heuristic_2
    path, cost = a_star_search(sequence, get_neighbors_func, 
            is_happy_pancakes, heuristic)
    goal = '1' * len(sequence)
    return cost[goal]

stdin = sys.stdin
num_cases = int(stdin.readline())

def parse_and_solve_case():
    pancake_sequence = stdin.readline()
    return find_cost(pancake_sequence.strip())

for case in range(num_cases):
    output = parse_and_solve_case()
    print 'case #{}: {}'.format(case+1, output)
