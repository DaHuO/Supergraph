import sys
import operator
import string

def decre_state(state, ans):
    for ch in ans:
        state[ch] = state[ch]  - 1
        if state[ch] == 0:
            del state[ch]
    return state

def evacuate(state, soln):
    while state:
        if len(state.keys()) ==2:
            if state.values()[0] == state.values()[1]:
                ans = ''.join(state.keys())
                soln.append(ans)
                state = decre_state(state, ans)
                continue
        for k, v in sorted(state.iteritems(), key=operator.itemgetter(1), reverse=True):
            ans = k
            soln.append(k)
            state = decre_state(state, ans)
            break
    return soln
    


if __name__ == '__main__':
    fpath = sys.argv[1]

    with open(fpath, 'r') as f:
        content = f.read()

    content = content.split('\n')

    t = int(content[0]) #no. of test cases
    cnt = 0
    for jj in range(1, 2*(t), 2):        
        cnt += 1
        party_state = content[jj+1].split(' ')
        
        state = {}
        for ii, n in enumerate(party_state):
           
            state[string.uppercase[ii]] = int(n)
        
        print 'Case #{}: {}'.format(cnt, ' '.join(evacuate(state, [])))
