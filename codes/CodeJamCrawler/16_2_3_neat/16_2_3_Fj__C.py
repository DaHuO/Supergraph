import pdb
import sys
import re
import time
from collections import namedtuple
from itertools import *
from copy import copy, deepcopy
from pprint import pprint
from glob import glob

taskname = 'C'
input_file = None


def readstr():
    return next(input_file).strip()


def readintlist():
    lst = list(map(int, readstr().split()))
    return lst


def readint():
    lst = readintlist()
    assert len(lst) == 1
    return lst[0]

def maxflow(graph, reverse_graph, capacity, source, sink):
    flow = dict((edge, 0) for edge, _ in capacity.items())
    def dfs():
        visited = {source: None}
        stack = [source]
        while stack:
            node = stack.pop()
            if node == sink:
                result = []
                while True:
                    point = visited[node]
                    if point is None:
                        return result
                    result.append(point)
                    node = point[0]
                
            for next in graph.get(node, []):
                if next in visited:
                    continue
                edge = (node, next)
                if capacity[edge] > flow[edge]:
                    visited[next] = (node, edge, True)
                    stack.append(next)
            for next in reverse_graph.get(node, []):
                if next in visited:
                    continue
                edge = (next, node)
                if flow[edge] > 0:
                    visited[next] = (node, edge, False)
                    stack.append(next)
        return None
    while True:
        path = dfs()
        if path is None:
#             print(sorted(flow.items()), '\n', [(node, flow[(source, node)]) for node in graph[source]])
            return sum(flow[(source, node)] for node in graph[source])
        # assume capacities are 0, 1
        for node, edge, direct in path:
            if direct:
                assert flow[edge] == 0
                flow[edge] += 1
            else:
                assert flow[edge] == 1
                flow[edge] -= 1


def greedy(word_pairs):
    ss1 = set(t[0] for t in word_pairs)
    ss2 = set(t[1] for t in word_pairs)
    for n in range(1, len(word_pairs) + 1):
        for chosen in combinations(word_pairs, n):
            s1 = set(t[0] for t in chosen)
            s2 = set(t[1] for t in chosen)
            if len(s1) == len(ss1) and len(s2) == len(ss2):
                return n
             
            

def solvecase():
    N = readint()
    word_pairs = []
    graph, reverse_graph, capacities = {}, {}, {}
    source, sink = '0', '1'
    def add_edge(node1, node2):
        if node2 in graph.setdefault(node1, []): return
        graph.setdefault(node1, []).append(node2)
        reverse_graph.setdefault(node2, []).append(node1)
        capacities[(node1, node2)] = 1
    for _ in range(N):
        w1, w2 = readstr().split()
        w1, w2 = '0' + w1, '1' + w2
        add_edge(source, w1)
        add_edge(w1, w2)
        add_edge(w2, sink)
        word_pairs.append((w1, w2))
    max_matching = maxflow(graph, reverse_graph, capacities, source, sink)
    min_basis = max_matching + len(graph[source]) - max_matching + len(reverse_graph[sink]) - max_matching
    result = N - min_basis
#     greedy_result = N - greedy(word_pairs)
#     if result != greedy_result:
#         print(graph[source])
#         print(result, greedy_result, N, max_matching, len(graph[source]), len(reverse_graph[sink]))
#         assert False
    return result
    


def solve(input_name, output_name):
    global input_file
    tstart = time.clock()
    with open(input_name, 'r') as input_file, open(output_name, 'w') as output_file:
        casecount = readint()
        
        for case in range(1, casecount + 1):
            s = solvecase()
            s = "Case #%d: %s" % (case, str(s)) 
            print(s, file=output_file)
            print(s) 
        
    print('%s solved in %.3f' % (input_name, time.clock() - tstart))


def main():
    input_names = glob(taskname + '-*.in')
    assert len(input_names)
    input_names.sort(reverse = True)
    for input_name in input_names:
        solve(input_name, input_name.replace('.in', '.out')) 
                

if __name__ == '__main__':
    main()
