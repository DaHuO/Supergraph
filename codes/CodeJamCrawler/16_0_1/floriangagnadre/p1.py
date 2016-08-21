def get_cases(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        cases = []
        for t in range(T):
            cases.append(int(f.readline()))
        return T, cases

def count_sheep(N):
    if N == 0:
        return 'INSOMNIA'
    count = N
    visited = [1 if str(x) in str(count) else 0 for x in range(10)]
    while sum(visited) < 10:
        count += N
        for c in str(count):
            visited[int(c)] = 1
    return count

def b_print(res, T, filename):
    with open(filename, 'w') as f:
        for t in range(T):
            f.write("Case #{0}: {1}\n".format(t+1, str(res[t])))

if __name__ == '__main__':
    filename = 'A-large.in.txt'
    T, cases = get_cases(filename)
    res = [count_sheep(N) for N in cases]
    b_print(res, T, 'outputp1-large.txt')