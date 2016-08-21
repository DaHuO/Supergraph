import csv
import concurrent.futures

def read_input(filename):
    r = csv.reader(open(filename, 'r', newline=''))
    next(r)
    inputs = []
    for row in r:
        inputs.append(int(row[0]))
    return inputs

def write_output(solutions, name):
    w = csv.writer(open(name, 'w', newline=''))
    for i, sol in enumerate(solution):
        w.writerow(['Case #' + str(i+1) + ':' + ' ' + str(sol)])

def get_nums(n):
    return set(list(str(n)))

def solve(n):
    if n == 0:
        return 'INSOMNIA'
    step = 1
    seen = get_nums(n)
    current = n
    while len(seen) < 10:
        current += n
        nums = get_nums(current)
        seen |= nums
        
    return current

def solve_list(ns):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        solutions = executor.map(solve, ns)
        return solutions

if __name__ == '__main__':
    inputs = read_input('A-large.in')
    solution = solve_list(inputs)
    write_output(solution, 'A-large.out')



        
