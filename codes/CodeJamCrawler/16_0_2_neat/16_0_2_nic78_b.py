import fileinput


def manipulate(state, i):
    """flips the first i pancakes and reverses their order"""
    return "".join(['-' if el == '+' else '+' for el in reversed(state[0:i])]) + state[i:]


def done(state):
    return state.find('-') == -1


def transitions(state):
    current = state[0]
    transitions = 0
    for c in state[1:]:
        if current!=c:
            transitions += 1
            current = c
    return transitions


def get_solution(line):
    #print
    #print
    #print line
    state = line.replace('\n', '')
    operations = 0
    states = [('', transitions(state), state)]
    n = len(state)
    seen = set()
    seen.add(state)
    while True:
        next_states = set()
        #print states        
        for (moves, t, state) in states:
            if done(state):
                return operations
            
            for i in range(1, n+1):
                newmove = moves+str(i)
                newstate = manipulate(state, i)
                newtransitions = transitions(newstate)
                if newtransitions<=transitions and not newstate in seen:
                    next_states.add((newmove, newtransitions, newstate))
                    seen.add(newstate)

        states = next_states
        operations += 1

        
def test_manipulate():
    print manipulate('++--', 1) # -+--
    print manipulate('++--', 3) # +---

    
if __name__ == '__main__':
    for (linenr, line) in enumerate(fileinput.input()):
        line = line[:-1]
        if fileinput.isfirstline():
            n = int(line)
            continue
        if linenr>n:
            print 'too many inputs'
            break

        print 'Case #%d: %s' % (linenr, get_solution(line))

    
    
    
