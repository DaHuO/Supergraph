def get_digits(n):
    ret = []
    while n > 9:
        n, mod = divmod(n, 10)
        ret.append(mod)
    ret.append(n)
    return set(ret)
    
def sheep(n):
    if n == 0: return 'INSOMNIA'
    digits = {x: True for x in range(10)}
    i = 0
    while digits:
        i += 1
        curr_digits = get_digits(n * i)
        for key in curr_digits:
            digits.pop(key, None)
        
    return n * i

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        n = int(raw_input())
        print "Case #{}: {}".format(i, sheep(n))

if __name__ == '__main__':
    main()