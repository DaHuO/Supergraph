from itertools import count

def last_num():
    n = int(input())
    if n == 0:
        return 'INSOMNIA'
    else:
        digits = list('0123456789')
        for i in count(1):
            for d in str(n * i):
                if d in digits:
                    digits.remove(d)
            if not digits:
                return n * i

for case in range(int(input())):
    print ('Case #{}: {}'.format(case+1, last_num()))
