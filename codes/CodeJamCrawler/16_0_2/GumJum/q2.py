
import sys

def s2b(s):
    return [x == '+' for x in s]

def flip(b, n):
    return [not x for x in b[n-1::-1]] + b[n:]

def getSuccessors(b):
    s = []
    for i in range(len(b)):
        s.append(flip(b, i+1))
    return s
    
def graphSearchGeneric(b, push, pop, empty):
    s = []
    if all(b):
        return 0
    [push(s,(x, 1)) for x in getSuccessors(b)]
    visited = [b]

    while not empty(s):
        v = pop(s)
        #print v
        if all(v[0]):
            #print v
            return v[1]
        
        if not v[0] in visited:
            successors = getSuccessors(v[0])
            visited.append(v[0])
            [push(s, (x, v[1] +1)) for x in successors]
    return -1
   
def getBlocksN(l):
    count = 0
    last = l[0]
    for x in l:
        if x != last:
            count += 1
            last = x
    return count
    
def shorten(b):
    count = 0
    n = [b[0]]
    last = b[0]
    for x in b:
        if x != last:
            n.append(x)
            last = x
    return n

def solveT(b):
    if (b[-1] == '+'):
        return len(b) - 1
    return len(b)
    
def main():
    to_write = ''
    with open(sys.argv[1], 'r') as f:
        first_line = f.readline()
        count = 0
        push = lambda s, x: s.append(x)
        pop = lambda s: s.pop(0)
        empty = lambda s: len(s) == 0
        
        for l in f:
            count += 1
            #tmp = shorten(s2b(l.strip()))
            c = solveT(shorten(l.strip()))
            #c = graphSearchGeneric(tmp, push, pop, empty)
            print(count, c)
            to_write += 'Case #' + str(count) + ': ' + str(c)
            to_write += '\n'
    
    with open(sys.argv[2], 'w') as f:
        f.write(to_write)
        
if __name__ == '__main__':
    main()