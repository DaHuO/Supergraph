#!/usr/bin/env python3
from time import sleep
from collections import Counter
FORMAT = "Case #{}: {}"

WORDS = "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
word_counters = [Counter(word) for word in WORDS]

class AStarGrid():

    def __init__(self):
        pass

    def generate_neighbors(self, p):
        n = []
        for d, w in enumerate(WORDS):
            s_word = "".join(sorted(p[0] + w))
            digit = p[1] + str(d)
            n.append((s_word, digit))
        return n

    def find_path_from(self, start, goal):
        open_list, closed_list = [start], []
        g, f, h, came_from = {}, {}, {}, {}
        g[start] = 0
        f[start] = AStarGrid.distance(start, goal)
        h[start] = f[start]
        while open_list:
            parent = min(open_list, key=f.get)
            if parent[0] == goal[0]:
                return AStarGrid.reconstruct_path(came_from, goal)
            open_list.remove(parent)
            closed_list.append(parent)
            for neighbor in self.generate_neighbors(parent):
                if neighbor in closed_list:
                    continue
                tmp_g = g[parent] + AStarGrid.distance(parent, neighbor)
                better = False
                if neighbor not in open_list:
                    open_list.append(neighbor)
                    better = True
                elif tmp_g < g[neighbor]:
                    better = True
                if better:
                    came_from[neighbor] = parent
                    g[neighbor] = tmp_g
                    h[neighbor] = AStarGrid.distance(neighbor, goal)
                    f[neighbor] = g[neighbor] + h[neighbor]

    def distance(p1, p2):
        s = 0
        for i in range(max(len(p1[0]), len(p2[0]))):
            if i >= len(p1[0]) or i >= len(p2[0]) or p1[0][i] != p2[0][i]:
                s += 1
        return s

    def reconstruct_path(came_from, current_node):
        for i in came_from.keys():
            if i[0] == current_node[0]:
                return i[1]

if __name__ == "__main__":
    cases = int(input())
    for t in range(cases):
        i = input()
        goal = Counter(i)
        grid = AStarGrid()
        path = grid.find_path_from(("", ""), ("".join(sorted(i)), ""))
        print(FORMAT.format(t + 1, "".join(sorted(path))))
