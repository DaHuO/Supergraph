def get_long_indexes(k, c):
    indexes = range(k)
    for i in range(k):
        for j in range(1, c):
            indexes[i] = k * indexes[i]
    return indexes
            

def solution(k, c, s):
    if s == k:
        return ' '.join([str(x + 1) for x in get_long_indexes(k, c)])
    else:
        return ' '.join([str(x + 1) for x in get_short_indexes(k, c)])
    
def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        k, c, s = [int(x) for x in str(raw_input()).split()]
        print "Case #{}: {}".format(i, solution(k, c, s))

if  __name__ == '__main__':
    main()