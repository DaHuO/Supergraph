
def ranknfile(file_in):
    fr = open(file_in, 'r')
    T = int(fr.readline().strip())
    fw = open(file_in[:-3] + '.out', 'w')
    
    for i in range(T):
        miss = []
        N = int(fr.readline().strip())
        S = []
        for j in range(2*N-1):
            S.extend(fr.readline().strip().split())
            
        for j in set(S):
            if S.count(j) % 2 != 0:
                miss.append(int(j))
                
#         print('Case #%d: '%(i+1), *sorted(miss))
        fw.write('Case #%d: '%(i+1) + ' '.join(str(i) for i in sorted(miss)) + '\n')

    fr.close()
    fw.close()


ranknfile('B-large.in')

