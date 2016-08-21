#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Google Code Jam: Round 1A 2016
# Problem C. BFFs
#
# by xenosoz on Apr 16, 2016.
#

from operator import attrgetter

class Cycle:
    def __init__(self, leader, rank):
        self.leader = leader
        self.rank = rank

class Path:
    def __init__(self, valid, leader, rank):
        self.valid = valid
        self.leader = leader
        self.rank = rank
                    
def solve():
    N = int(input())
    F = [int(x) - 1 for x in input().split()]
    assert N == len(F)

    def make_group(n):
        # n-th node is in cycle? (in a dirty way)
        current = n
        min_node = n
        for cycle_length in range(1, N+1):
            current = F[current]
            min_node = min(min_node, current)
            if n == current:
                return Cycle(min_node, cycle_length)
        return Cycle(min_node, 0)

    groups = list(map(make_group, range(N)))
    
    # Case 1: Everyone is in a large group.
    case_1_max = max(map(attrgetter('rank'), groups))

    # Case 2: Can partition it as O -> O -> (O <-> O) <- O <- O.
    paths = [None] * N
    def follow_path(n):
        if paths[n] is not None:
            return paths[n]
        
        if groups[n].rank == 2:
            new_p = Path(True, n, 0)
            paths[n] = new_p
            return new_p

        if groups[n].rank != 0:
            new_p = Path(False, -1, -1)
            paths[n] = new_p
            return new_p

        p = follow_path(F[n])
        if not p.valid:
            new_p = Path(False, -1, -1)
            paths[n] = new_p
            return new_p

        new_p = Path(True, p.leader, p.rank + 1)
        paths[n] = new_p
        return new_p

    for c in range(N):
        follow_path(c)

    longest_path = [0] * N
    for c in range(N):
        longest_path[paths[c].leader] = max(longest_path[paths[c].leader], paths[c].rank)

    case_2_max = 0
    for c in range(N):
        g = groups[c]
        if g.rank != 2:
            continue
        left = c
        right = F[c]
        score = longest_path[left] + g.rank + longest_path[right]
        case_2_max += score

    assert case_2_max % 2 == 0        
    case_2_max //= 2
    
    return max(case_1_max, case_2_max)
        

T = int(input())

for case_id in range(1, T+1):
    print("Case #%d:" % case_id, solve())
