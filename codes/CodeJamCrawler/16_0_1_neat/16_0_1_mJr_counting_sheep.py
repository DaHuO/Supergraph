def main():
    T = input()
    for t in range(T):
        N = input()
        print "Case #%d: %s" % (t+1,str(get_result(N)))

def get_result(N):
    if N == 0: return 'INSOMNIA'
    visited = set()
    return get_last_number(N, visited)

def get_last_number(N, visited):
    n = N
    while True:
        visited.update({d for d in str(n)})
        if len(visited) == 10: return n
        n += N

if __name__ == '__main__': main()