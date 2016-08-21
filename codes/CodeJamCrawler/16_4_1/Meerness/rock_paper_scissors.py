__author__ = 'User'

winner_tree = {
    "R": ["R", "S"],
    "P": ["P", "R"],
    "S": ["S", "P"]
}


def make_prs_tree(N, n_R, n_P, n_S):
    solutions = []
    ordered_solutions = []
    for winner in ["R", "P", "S"]:
        solutions.append(build_recursive_solution(winner, N))
    for solution in solutions:
        if solution.count("R") != n_R:
            continue
        if solution.count("P") != n_P:
            continue
        if solution.count("S") != n_S:
            continue
        ordered_solutions.append(solution)
    if not ordered_solutions:
        return "IMPOSSIBLE"
    return "".join(sorted(ordered_solutions)[0])


def build_recursive_solution(winner, depth):
    if depth == 1:
        return sorted(winner_tree[winner])
    prevs = winner_tree[winner]
    sol1 = build_recursive_solution(prevs[0], depth - 1)
    sol2 = build_recursive_solution(prevs[1], depth - 1)
    if sol1 > sol2:
        return sol2 + sol1
    return sol1 + sol2

with open("input.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            input_list = line.strip().split(' ')
            x = make_prs_tree(*[int(x) for x in input_list])
            write_file.write("Case #" + str(i) + ": " + x + "\n")