import sys
import utils

fname = sys.argv[1]

def get_ans(case):
    n = case[0]

    if n == 0:
        return 'INSOMNIA'

    digset = set()
    curr_n = 0

    while len(digset) < 10:
        curr_n += n
        copy_n = curr_n
        
        while copy_n:
            dig = copy_n % 10
            digset.add(dig)
            copy_n /= 10

    return curr_n    

utils.process(fname, 1, [lambda x: int(x)], get_ans)
