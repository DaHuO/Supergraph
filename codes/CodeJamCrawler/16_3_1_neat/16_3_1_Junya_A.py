def print_solution(i, indices):
    new_indices = [''.join([chr(x+65) for x in xs]) for xs in  indices]
    solution = ' '.join(new_indices)
    print 'Case #{}: {}'.format(i, solution)

def get_biggest(p):
    max_index = 0
    max_value = 0
    for i, v in enumerate(p):
        if v > max_value:
            max_value = v
            max_index = i
    if max_value <= 0:
        raise Exception('get biggest returned 0 value')        
    return max_index
        
def get_next(p, total):
    indices = []
    if sum(p) % 2 == 0:
        index = get_biggest(p)
        p[index] -= 1
        indices.append(index)
        total -= 1
    index = get_biggest(p)
    p[index] -= 1
    indices.append(index)
    total -= 1
    return indices, p, total

def handle_case(i):
    N = int(raw_input())
    p = map(int, raw_input().split())
    solution = []
    total = sum(p)
    while total > 0:
        indices, p, total = get_next(p, total)
        solution.append(indices)
    print_solution(i, solution)
        
def main():
    T = int(raw_input())
    for i in range(T):
        handle_case(i + 1)

if __name__ == "__main__":
    main()    
