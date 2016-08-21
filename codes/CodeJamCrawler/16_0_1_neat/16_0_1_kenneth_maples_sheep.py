
def digits(k):
    if k < 10:
        return {k}
    return {k % 10}.union(digits(k / 10))

def sheep(n):
    m = n
    dd = digits(n)
    k = 0
    while dd != {0,1,2,3,4,5,6,7,8,9} and k <= 1000000:
        m += n
        dd = dd.union(digits(m))
        k += 1

    if k < 1000000:
        return str(m)
    else:
        return 'INSOMNIA'
    
def main():
    t = int(raw_input())
    for k in range(t):
        n = int(raw_input())
        print 'Case #' + str(k+1) + ': ' + sheep(n)
        
if __name__ == '__main__':
    main()
    
