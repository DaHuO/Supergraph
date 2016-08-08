#! /usr/bin/env python3
newline = False


def read_problem():
    return map(int, input().split())


def sort1(tree):
    try:
        left, right = tree
    except TypeError:
        return [tree]
    leftlist = sort(left)
    rightlist = sort(right)
    if leftlist > rightlist:
        tree[0], tree[1] = right, left
        return rightlist + leftlist
    else:
        return leftlist + rightlist


def sort(tree):
    # returns (p, r, s, factor, value)
    try:
        left, right = tree
    except TypeError:
        return (int(tree == 0), int(tree == 1), int(tree == 2), 3, tree)
    sortleft = sort(left)
    sortright = sort(right)
    p = sortleft[0] + sortright[0]
    r = sortleft[1] + sortright[1]
    s = sortleft[2] + sortright[2]
    factor = sortleft[3]
    if sortleft[4] > sortright[4]:
        tree[0], tree[1] = right, left
        value = sortright[4] * factor + sortleft[4]
    else:
        value = sortleft[4] * factor + sortright[4]
    return (p, r, s, factor * factor, value)


def build_tree(root, n):
    if n == 0:
        return root
    elif root == 0:
        return [build_tree(0, n - 1), build_tree(1, n - 1)]
    elif root == 1:
        return [build_tree(1, n - 1), build_tree(2, n - 1)]
    else:
        return [build_tree(0, n - 1), build_tree(2, n - 1)]


def counts(l):
    c = [0] * 3
    for i in l:
        c[i] += 1
    return c


def treelist(tree):
    try:
        left, right = tree
    except TypeError:
        return [tree]
    return treelist(left) + treelist(right)


def solve(problem):
    n, r, p, s = problem
    ptree = build_tree(0, n)
    psort = sort(ptree)
    if psort[:3] == (p, r, s):
        return treelist(ptree)
    rtree = build_tree(1, n)
    rsort = sort(rtree)
    if rsort[:3] == (p, r, s):
        return treelist(rtree)
    stree = build_tree(2, n)
    ssort = sort(stree)
    if ssort[:3] == (p, r, s):
        return treelist(stree)
    return None


def print_solution(solution):
    if solution is None:
        print("IMPOSSIBLE")
    else:
        print(''.join("PRS"[i] for i in solution))


cases = int(input())
for n in range(1, cases + 1):
    problem = read_problem()
    solution = solve(problem)
    print("Case #{0}:".format(n), end='\n' if newline else ' ')
    print_solution(solution)
