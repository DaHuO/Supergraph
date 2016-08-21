

T = int(raw_input())

def get_check_location(loc, K, C):
    C = min(C, K)
    check_location = 0
    for i in xrange(0, C):
        check_location += (loc+i-1) * ( K ** (C-i-1) )
        if (loc+i >= K):
            break
    check_location += 1
    return check_location



for t in xrange(1, T+1):
    K, C, S = [int(x.strip()) for x in raw_input().split()]
    if K/C > S:
        print('Case #%d: IMPOSSIBLE' %(t))
        continue
    locations = []
    for loc in xrange(1, K+1, C):
        locations.append(get_check_location(loc, K, C))
    solutions_str = 'Case #%d:' %(t)
    for location in locations:
        solutions_str += ' %d' %(location)
    print(solutions_str)
        

        
"""
# TESTING CODE

def make_fractal(start, C):
    cur_pattern = start
    for i in xrange(1, C):
        print(cur_pattern)
        new_pattern = ''
        for c in start:
            if c == 'L':
                new_pattern += cur_pattern
            else:
                new_pattern += 'G' * len(cur_pattern)
        cur_pattern = new_pattern
    return cur_pattern


print(make_fractal('LLLLG', 2))
"""



