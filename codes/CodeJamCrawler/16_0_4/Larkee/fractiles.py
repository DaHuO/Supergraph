def fractiles(filename):
    file = open(filename, 'r')
    source = file.read()
    lines = source.splitlines()
    file.close()
    file = open('fractiles.txt', 'w')
    T = int(lines[0])
    for i in range(T):
        K, C, S = lines[i+1].split()
        file.write('Case #' + str(i+1) + ':')
        for j in range(int(K)):
            file.write(' ' + str(j+1))
        file.write('\n')
    file.close()

fractiles('D-small-attempt0.in')
