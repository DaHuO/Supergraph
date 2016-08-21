#! /usr/bin/python
import sys

def add_seen_digits(set, num):
    map(lambda digit: set.add(digit), str(num))
    return set

if __name__ == '__main__':
    # get path to input file
    data_file = sys.argv[1]

    # load input data
    with open(data_file) as fd:
        fd.readline()
        Ns = [int(n) for n in fd]

    # solve
    results = []
    for idx, n in enumerate(Ns):
        result = ''
        if n == 0:
            result = 'INSOMNIA'
        else:
            multi = 1
            current_n = n
            seen_digits = set([])
            while True:
                current_n = n * multi 
                add_seen_digits(seen_digits, current_n)
                if len(seen_digits) == 10:
                    result = str(current_n)
                    break
                multi += 1
        results.append(result)
    
    with open('counting_sheep_results.txt', 'w') as fd:
        for idx, result in enumerate(results):
            fd.write('Case #{}: {}\n'.format(idx+1, result))
            print 'Case #{}: {}'.format(idx+1, result)
        
    #    with


