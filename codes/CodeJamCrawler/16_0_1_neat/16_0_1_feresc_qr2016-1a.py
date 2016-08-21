#!python
def solve(N):
    s = set()
    for m in range(1,100000):
        s.update(set(str(m*N)))
        if len(s) == 10:
            return m*N
    return 'INSOMNIA'
        

def main():
    n = int(raw_input())
    for c in range(1, n + 1):
        N = int(raw_input())
        res = solve(N)
        print 'Case #%d: %s' % (c, res)
    
if __name__ == "__main__":
  main()
    
