from itertools import product

def add_complexity(string, original_string):
    new_string = ""
    for c in string:
        if c=='L':
            new_string+=original_string
        elif c=='G':
            new_string+=('G'*len(original_string))
    return new_string

def tiles_to_check(start, complexity, grad_students):
    possibilities = product('LG', repeat=start)
    possibilities = [''.join(x) for x in possibilities]
    endings = []
    for p in possibilities:
        current = p
        for i in xrange(complexity):
            current = add_complexity(current, p)
        endings.append(current)
    return endings

def p4_small():
    with open('small.in') as f:
        cases = f.read().splitlines()[1:]

    case_number = 1
    for case in cases:
        c = case.split()
        tiles = range(1,int(c[0])+1)
        tiles = " ".join([str(x) for x in tiles])
        print "Case #{}: {}".format(str(case_number),tiles)
        case_number+=1

if __name__=='__main__':
    p4_small()