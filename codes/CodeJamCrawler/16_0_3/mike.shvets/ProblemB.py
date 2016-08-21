import numpy as np

with open('input.txt') as f:
    T = int(next(f))
    N, J = [int(x) for x in next(f).split()]


with open('output.txt', 'w+') as f:
    f.write('Case #1:\n')
    
    count = 0
    jams = []
    while count < J:
        cur = '1' + ''.join(map(str, np.random.binomial(1, 0.5, N-2))) +  '1'
        while cur in jams:
            cur = '1' + ''.join(map(str, np.random.binomial(1, 0.5, N-2))) +  '1'

        flag = True
        divs = np.zeros(9, dtype='int64')
        for k in range(2, 11):
            num = int(cur, base=k)

            if num % 2 == 0:
                divs[k-2] = 2
                continue

            div = 3
            while div*div <= min(num, 100000):
                if num % div == 0:
                    divs[k-2] = div
                    break
                div += 1

            if divs[k-2] == 0:
                flag = False
                break
                
        if flag:
            count += 1
            jams.append(cur)
            f.write(cur + ' ' + ' '.join(map(str, divs)) + '\n')
            
            #print '%d numbers found' %count

    
