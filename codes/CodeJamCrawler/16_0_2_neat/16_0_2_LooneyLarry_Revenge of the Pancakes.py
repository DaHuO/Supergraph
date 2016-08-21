# Google Code Jam 2016 Qualifying B
# Strategy: If top is -, flip whole stack.  If +, flip consecutive +.
# Don't need to record number of consecutive happy or unhappy
# pancakes, only number of transitions and whether top pancake is
# happy.  Here are some stacks, encodings (as happy and #transitions)
# and number of flips needed:
# +++ +0 0
# --- -0 1
# +-- +1 2
# --+ -1 1
# Using t as number of transitions, note that number of flips is t,
# with an additional flip if happy and odd(t) or not happy and
# even(t).
def odd(num):
    return num % 2
def numFlips(happyTop, numTransitions):
    return numTransitions + (1 if happyTop and odd(numTransitions) or
                             not happyTop and not odd(numTransitions) else 0)
def doCase(stack):
    transitions = 0
    for i in range(len(stack) - 1):
        if stack[i] != stack[i+1]:
            transitions += 1
    return numFlips(stack[0] == '+', transitions)

cases = int(raw_input())
for i in range(cases):
    print 'Case #{}: {}'.format(i+1, doCase(raw_input().strip()))
