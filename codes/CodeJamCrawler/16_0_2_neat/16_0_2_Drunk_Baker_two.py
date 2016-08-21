import csv
import sys
import concurrent.futures

def read_input(filename):
    r = csv.reader(open(filename, 'r', newline=''))
    next(r)
    inputs = []
    for row in r:
        inputs.append(list(reversed(row[0])))
    return inputs

def print_output(filename, outputs):
    w = csv.writer(open(filename, 'w', newline=''))
    for i, output in enumerate(outputs):
        w.writerow(['Case #' + str(i+1) + ': ' + str(output)])

class stack:
    def __init__(this, cakes, flips=0):
        this.__cakes = cakes
        this.__flips = flips

    def flip(this,n):
        this.__flips += 1
        
        this.__cakes = this.__cakes[:-1*n] + list(map(lambda x : '+' if x == '-' else '-', this.__cakes[-1*n:]))

    def get_flips(this):
        return this.__flips

    def get_len(this):
        return len(this.__cakes)

    def copy(this):
        return stack(this.__cakes, this.__flips) 

    def get_cakes(this):
        return this.__cakes

    def __simplify(this):
        i = 0
        while i < len(this.__cakes) and this.__cakes[i] == '+':
            i += 1
        this.__cakes = this.__cakes[i:]

    def is_done(this):
       this.__simplify()
       return len(this.__cakes) == 0


def solve(s, seen_stacks = None):
    if seen_stacks == None:
        seen_stacks = set()

    if s.is_done():
        return s.get_flips()

    if ''.join(s.get_cakes()) in seen_stacks:
        return None
    seen_stacks.add(''.join(s.get_cakes()))

    cakes = [] 
    for i in range(s.get_len(), 0, -1):
        cake = s.copy()
        cake.flip(i)
        cakes.append(cake)

    values = list(filter(lambda x : x != None, map(lambda x : solve(x, seen_stacks), cakes)))
    if len(values) == 0:
        return None
    return min(values)

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    inputs = list(map(lambda x : stack(x), read_input('B-small-attempt0.in')))
    outputs = list(map(solve, inputs))
    print_output('B-small-0.out', outputs)


