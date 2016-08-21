# Google Code Jam Qualification Round 2016
# Problem A. Counting Sheep

def sheep(N):
    if N == 0:
        return 'INSOMNIA'
    seen = []
    current = 0
    while len(seen) != 10:
        current += N
        for i in str(current):
            d = int(i)
            seen += (d not in seen)*[d]
    return str(current)

def beatrix():
    f = open('commands.txt', 'r')
    g = open('sheep.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            g.write('Case #' + str(line) + ': ')
            g.write(sheep(int(i)))
            g.write((T != line)*'\n')
            line += 1
    f.close()
    g.close()
            
