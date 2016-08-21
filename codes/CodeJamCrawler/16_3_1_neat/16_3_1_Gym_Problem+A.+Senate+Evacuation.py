
def evacuation(file_in):
    fr = open(file_in, 'r')
    T = int(fr.readline().strip())
    fw = open(file_in[:-3] + '.out', 'w')
    
    for i in range(T):
        parties_name = 'ABCEFGHIJKLMNOPQRSTUVWXYZ'
        N = int(fr.readline().strip())
        parties = [int(j) for j in fr.readline().strip().split()]
        plan = []
        while sum(parties) != len(parties):
            ind_max = parties.index(max(parties))
            plan.append(parties_name[ind_max])
            parties[ind_max] -= 1
        
        nleft = len(parties)
        if nleft % 2 != 0:
            nleft -= 1
            plan.append(parties_name[nleft])
        
        for j in range(int(nleft/2)):
                plan.append(parties_name[2*j:2*j+2])
            
#         print('Case #%d: '%(i+1) + ' '.join(plan))
        fw.write('Case #%d: '%(i+1) + 'Case #%d: '%(i+1) + ' '.join(plan) + '\n')

    fr.close()
    fw.close()

evacuation('A-large.in')

