import fileinput

def flip(pancakes):
    n = len(pancakes)
    cnt = 0
    if sum(pancakes) == n:
        return 0
    if sum(pancakes) == 0:
        return 1
    
    while pancakes[-1] == 1:
        pancakes = pancakes[-1]
    

def count_flip(pancakes):
    # print pancakes
    
    n = len(pancakes)
    ps = pancakes
    cnt = 0

    if n == 1:
        if sum(pancakes) == 0:
            return 1
        elif sum(pancakes) == 1:
            return 0

    if ps[-1] == 1:
        cnt += count_flip(ps[:-1])
    elif ps[0] == 1:
        cnt += 1
        cnt += count_flip(ps[::-1])
    elif ps[0] == 0:
        cnt += 1 # FLIP THE TOP( ==discard the top)
        cnt += 1 # flip the whole
        cnt += count_flip(ps[1:][::-1])
    return cnt

def compress(pancakes):
    new = []
    lp = -1
    for p in pancakes:
        if p != lp:
            new.append(p)
            lp = p

    return new

def main():
    # inputs = [0, 1, 2, 11, 1692]s
    inputs = []
    
    for line in fileinput.input():
        inputs.append(line.strip())
    inputs = inputs[1:]

    pancakes_list = []
    for i in inputs:
        pancakes = []
        for c in i:
            if c == '+':
                pancakes.append(1)
            else:
                pancakes.append(0)
        pancakes = compress(pancakes)
        pancakes_list.append(pancakes)            


    for i, pancakes in enumerate(pancakes_list):
        # print 'before:', pancakes
        cnt = count_flip(pancakes)
        print 'Case #%d: %d' % (i+1, cnt)

if __name__ == '__main__':
    main()
