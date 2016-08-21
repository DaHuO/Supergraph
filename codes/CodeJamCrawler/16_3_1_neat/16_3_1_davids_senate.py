from __future__ import print_function, division
import sys
from collections import defaultdict, Hashable
from functools import partial
from random import shuffle, choice, randint
import heapq
from itertools import izip,groupby,product,combinations
from math import sqrt, ceil, floor
from string import ascii_uppercase
class heap:
    def __init__(self, node):
        self.nodes = []
        heapq.heappush(self.nodes, (0, node))
    
    def empty(self):
        return len(self.nodes) == 0
    
    def push(self, node, priority):
        heapq.heappush(self.nodes, (priority, node))
    
    def pop(self):
        return heapq.heappop(self.nodes)[1]
        
def read_case(f):
    n = int(f.readline().rstrip())
    parties = tuple(map(int, f.readline().rstrip().split(' ')))
    return parties

in_ = open(sys.argv[1], 'r')
num_cases = int(in_.readline())
cases = [read_case(in_) for n in range(num_cases)]
"""
cases = []
while len(cases) < 100:
    m = randint(1,26)
    parties = [randint(0, 1000) for i in range(m)]
    n = sum(parties)
    maj = n / 2
    good = True
    for j in range(m):
        if parties[j] > maj:
            good = False
    if good:
        cases.append(tuple(parties))
"""        
def print_case(result, n, f):
    text = "Case #%d: %s" % (n, result)
    out.write(text + '\n')
    print(text)

def options(cur):
    num_parties = len(cur)
    
    for i in range(num_parties):
        if cur[i] > 0:
            after= list(cur)
            after[i] -= 1
            n = sum(after)
            maj = n / 2
            good = True
            for j in range(num_parties):
                if after[j] > maj:
                    good = False
            if good:
                yield (ascii_uppercase[i], tuple(after))
        if cur[i] > 1:
            after= list(cur)
            after[i] -= 2
            n = sum(after)
            maj = n / 2
            good = True
            for j in range(num_parties):
                if after[j] > maj:
                    good = False
            if good:
                yield (2*ascii_uppercase[i], tuple(after))
    for a,b in combinations(range(num_parties), 2):
        if cur[a] > 0 and cur[b] > 0:
            after = list(cur)
            after[a] -=1
            after[b] -=1
            n = sum(after)
            maj = n / 2
            good = True
            for j in range(num_parties):
                if after[j] > maj:
                    good = False
            if good:
                yield (ascii_uppercase[a]+ascii_uppercase[b], tuple(after))
    
def do_case(case):
    parties = case
    num_parties = len(parties)
    total = sum(parties)
    steps = []
    goal = tuple([0 for i in range(num_parties)])
    open_set = heap(parties)
    closed_set = set()
    g = defaultdict(lambda: 10**10)
    came_from = {}
    did = {}
    g[parties] = 0
    #f = defaultdict(lambda: 10**10)
    eval_count = 0
    while not open_set.empty():
        cur = open_set.pop()
        eval_count+=1
        if cur == goal:
            break
        closed_set.add(cur)
        
        neighbors = options(cur)
        for step, neighbor in neighbors:
                       
            new_score = g[cur] 
            if neighbor not in closed_set and new_score < g[neighbor]:
                open_set.push(neighbor, new_score + sum(neighbor))
                g[neighbor] = new_score
                came_from[neighbor] = cur
                did[neighbor] = step
                #print(cur, 'pushed', step, neighbor)
                #print('pushed', flipped, new_score)
    print('evals:', eval_count)
    steps = []
    i = goal
    while i != parties:
        steps.append(did[i])
        i = came_from[i]
    print(' '.join(steps[::-1]))
    return ' '.join(steps[::-1])
    
results = [do_case(case) for case in cases]

out = open(sys.argv[2], 'w')
for n,result in enumerate(results):
    print_case(result, n+1, out)
