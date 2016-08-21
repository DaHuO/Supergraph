from __future__ import print_function
import heapq


def gen_graph(N):
    def to_digits(n):
        digits = [0] * N
        step = 0
        while n > 0:
            step += -1
            digits[step] = n % 2
            n //= 2
        return digits

    def from_digits(digits, b=2):
        n = 0
        for d in digits:
            n = b * n + d
        return n

    graph = {}
    for vertex in xrange(0, 2 ** N):
        path = set()
        digits = to_digits(vertex)
        for i in xrange(1, N + 1):
            tmp_digits = digits[:]
            for j in xrange(0, i):
                tmp_digits[j] = 0 if tmp_digits[j] == 1 else 1
            path.add(from_digits(tmp_digits))
        graph[vertex] = path
    return graph


# def shortest_path(graph, start, goal):
#     def bfs_paths(graph, start, goal):
#         queue = [(start, [start])]
#         while queue:
#             (vertex, path) = queue.pop(0)
#             for next in graph[vertex] - set(path):
#                 if next == goal:
#                     yield path + [next]
#                 else:
#                     queue.append((next, path + [next]))
#
#     try:
#         return next(bfs_paths(graph, start, goal))
#     except StopIteration:
#         return [goal]

def shortest_path(G, start, end):
    def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
        while len(L) > 0:
            yield L[0]
            L = L[1]

    q = [(0, start, ())]  # Heap of (cost, path_head, path_rest).
    visited = set()       # Visited vertices.
    while True:
        (cost, v1, path) = heapq.heappop(q)
        if v1 not in visited:
            visited.add(v1)
            if v1 == end:
                return list(flatten(path))[::-1] + [v1]
            path = (v1, path)
            for v2 in G[v1]:
                if v2 not in visited:
                    heapq.heappush(q, (cost + 1, v2, path))

Nmax = 10
graphs ={}
for n in xrange(1, Nmax + 1):
    graphs[n] = gen_graph(n)


with open('B-small-attempt1.in', 'r') as inp, open('ans3.txt', 'w') as out:
    T = int(inp.readline())
    case = 0
    for line in inp:
        case += 1
        N = len(line) - 1
        vertex = int(line.replace('-', '0').replace('+', '1'), 2)
        ans = len(shortest_path(graphs[N], vertex, 2 ** N - 1)) - 1
        print('Case #{0}: {1}'.format(case, ans), file=out)
