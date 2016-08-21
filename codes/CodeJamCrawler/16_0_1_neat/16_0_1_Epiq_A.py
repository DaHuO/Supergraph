def solve():
    n = int(raw_input())
    
    if n == 0:
        return 'INSOMNIA'
    
    d = {}
    t = 0
    while len(d) < 10:
        t += n
        
        dig = [int(x) for x in str(t)]
        
        for x in dig:
            if d.has_key(x):
                d[x] += 1
            else:
                d[x] = 1
    
    return t

def main():
    T = int(raw_input())
    
    for t in range(1, T + 1):
        print 'Case #%d:' % t, solve()


if __name__ == '__main__':
    main()