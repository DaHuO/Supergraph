import math

global result

def all_visited(visited):
    for t in visited:
        if not t:
            return False
    return True

def enum(N, F, i, cycle):
    bff_of_i = F[i]
    bff_of_bff = F[bff_of_i]
    if bff_of_i in cycle:
        # bff of I is in cycle
        if bff_of_bff == i:
            # bff of I is I, so I can sit with anyone next
            for t in range(N):
                if not t in cycle: # t is not in cycle
                    cycle.append(t)
                    enum(N, F, t, cycle)
                    cycle.pop()
        else:
            # finish, be a cycle
            global result
            index = cycle.index(bff_of_i)
            result = max(result, len(cycle) - index)
            print F, cycle, len(cycle) - index, index
    else:
        cycle.append(bff_of_i)
        enum(N, F, bff_of_i, cycle)
        cycle.pop()

# longest path
def search(N, m, i, visited):
    depth = 1
    for j in m[i]:
        if not visited[j]:
            visited[j] = True
            depth = max(depth, search(N, m, j, visited) + 1)
            visited[j] = False
    return depth

def solve(N, F):
    global result
    result = 0
    for i in range(N):
        enum(N, F, i, [i])

    reverse_map = [[] for i in range(N)]
    for i in range(N):
        reverse_map[F[i]].append(i)

    visited = [False for i in range(N)]
    result_for_btt_of_btt_is_me = 0
    for i in range(N):
        if not visited[i] and not visited[F[F[i]]] and F[F[i]] == i:
            visited[i] = True
            visited[F[i]] = True
            print i, F[i]
            result_for_btt_of_btt_is_me += search(N, reverse_map, i, visited)
            print result_for_btt_of_btt_is_me
            result_for_btt_of_btt_is_me += search(N, reverse_map, F[i], visited)
            print result_for_btt_of_btt_is_me
    return max(result, result_for_btt_of_btt_is_me)

with open('bff.in', 'r') as fin:
    with open('bff.out', 'w') as fout:
        T = int(fin.readline())
        for i in xrange(1, T+1):
            N = int(fin.readline())
            F = [int(c) - 1 for c in fin.readline().split(' ')]
            fout.write('Case #{0}: {1}\n'.format(i, solve(N, F)))
