#!/usr/bin/env python

def check_for_s(reveals,S):
    if len(reveals) > S:
        return 'IMPOSSIBLE'
    else:
        return ' '.join(reveals)

def solve(K,C,S):
    num_of_tiles = K**C
    step = (K**(C-1))
    reveals = []
    track = 1

    while track <= num_of_tiles:
        reveals.append('%s' % (track))
        track = track + step
    return check_for_s(reveals,S)


if __name__ == '__main__':
    in_file = '../Downloads/D-small-attempt2.in'
    in_file = open(in_file,'r')
    T = int(in_file.readline())
    
    out_file = open('out','w')

    for i in range(1,T+1):
        K,C,S = in_file.readline().split(' ')
        out_file.write('Case #%s: %s\n' 
                % (
                    i,
                    solve(int(K),int(C),int(S))
                )
        )
    in_file.close()
    out_file.close()
