#import heapq

def count_sheep(n):
    if n == 0: return -1
    
    total = n
    digits = [int(d) for d in str(total)]
    while len(set(digits)) < 10:
        total += n
        digits.extend([int(d) for d in str(total)])
    return total
        
if __name__ == '__main__':
    for T in range(int(raw_input())):
        n = int(raw_input().strip())
        n_sleep = count_sheep(n)
        if n_sleep < 0: print "Case #%d: INSOMNIA" % (T+1)
        else: print "Case #%d: %d" % (T+1, n_sleep)