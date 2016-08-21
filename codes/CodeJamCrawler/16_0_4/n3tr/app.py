

def generate_pattern(p,c=3):
    max_str = '1' * p
    max_val = int(max_str, 2)

    for i in xrange(0, max_val+1):
        n = "{0:b}".format(i)
        if len(n) < len(max_str):
            n = ('0' * (len(max_str) - len(n))) + n
        n = n.replace('1','L').replace('0','G')

        p = n
        for i in range(1, c):
            p = p.replace('G','G' * len(n)).replace('L',n)

        print p



def read_file():
    f = open('4-small.in', 'r')
    return f.read().splitlines()


lines = read_file()
t = int(lines[0])  # read a line with a single integer
for i in xrange(1, t + 1):
    line = lines[i]
    comp = line.split(' ')
    K, C, S = int(comp[0]), comp[1], comp[2]
    print "Case #{}: {}".format(i, ' '.join([str(n) for n in range(1, K+1)]))
