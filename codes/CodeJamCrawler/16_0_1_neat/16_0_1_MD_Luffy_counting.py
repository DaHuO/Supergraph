def digitize(number):
    while number:
        digit = number % 10
        yield digit
        number //= 10
    
def solve(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        hsh = [0]*10
        stop = False
        number = n
        while(True):

            for digit in digitize(number):
                hsh[digit] = 1
            
            if 0 not in hsh:
                return number
            number += n
        return number

def save(results, fpath):
    with open(fpath, 'w') as f:
        for i, res in enumerate(results):
            f.write('Case #{}: {}\n'.format(i+1, res))


if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        print 'Case #{}: {}'.format(i+1, solve(n)) 