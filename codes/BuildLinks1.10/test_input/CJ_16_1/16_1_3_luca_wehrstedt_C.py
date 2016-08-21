#!/usr/bin/python3

from collections import deque

def run():
    n = int(input().strip())
    graph = list(int(x) - 1 for x in input().split())
    reverse = list([] for _ in range(n))
    for i, j in enumerate(graph):
        reverse[j].append(i)

    res = -1

    twos = 0

    def depth(i):
        return max([0] + [depth(k) + 1 for k in reverse[i]])

    visited = n * [False]
    active = None
    stack = None
    for i in range(n):
        if visited[i]:
            continue
        active = n * [False]
        active[i] = True
        visited[i] = True
        again = False
        stack = [i]
        while not active[graph[stack[-1]]]:
            node = graph[stack[-1]]
            if visited[node]:
                again = True
                break
            visited[node] = True
            active[node] = True
            stack.append(node)
        if again:
            continue
        loop = stack[stack.index(graph[stack[-1]]):]
        if len(loop) == 2:
            distance2 = n * [None]
            queue = deque()
            reverse[loop[0]].remove(loop[1])
            reverse[loop[1]].remove(loop[0])
            twos += len(loop) + depth(loop[0]) + depth(loop[1])
        else:
            res = max(res, len(loop))

    return max(res, twos)


t = int(input().strip())
for i in range(t):
    print("Case #%d: %s" % (i+1, run()))
