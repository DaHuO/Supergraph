import math

f = open('input.in')
g = open('output', 'w')

T = int(f.readline()[:-1])

for case in range(T) :
    K, C, S = map(int, f.readline()[:-1].split())
    if K == 1 : res = [1]
    elif C == 1 : res = list(range(1, K+1))
    else : res = list(range(2, K+1))
    res = ' '.join(map(str, res))
    output = 'Case #' + str(case+1) + ': ' + str(res)
    print(output)
    g.write(output + '\n')

f.close()
g.close()
