f = open('A-small-attempt0.in')
g = open('small.out', 'w')

case = 0
T = int(f.readline()[:-1])

for line in f :
    case += 1
    line = line[:-1]
    N = int(line)
    seen = set()
    for i in range(1, 10001) :
        for d in str(i*N) :
            seen.add(d)
        if len(seen) == 10 :
            break
    res = i*N if i != 10000 else 'INSOMNIA'
    output = 'Case #' + str(case) + ': ' + str(res)
    print(output)
    g.write(output + '\n')

f.close()
g.close()
