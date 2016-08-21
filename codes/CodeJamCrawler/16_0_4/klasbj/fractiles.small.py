import sys

def solve(k, c, s):
    try:
        assert(k == s) # small input
        return ' '.join(str(x) for x in range(1,s+1))
    except:
        return 'IMPOSSIBLE' # for the example input

if __name__ == '__main__':
    for t,l in enumerate(sys.stdin.readlines()[1:]):
        print('Case #{}: {}'.format(t+1, solve(*(int(x) for x in l.split()))))
