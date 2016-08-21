def flip_count(state):
    if state.count('+') == len(state):
        return 0
    elif state.count('-') == len(state):
        for i in range(len(state)):
            state[i] = '+'
        return 1
    elif len(state) == 1:
        if state[0] == '+':
            return 0
        else:
            state[0] = '+'
            return 1
    else:
        if state[-1] == '-':  # flip everything
            length = len(state)
            for i in range(length):
                if state[i] == '-':
                    state[i] = '+'
                else:
                    state[i] = '-'
            inc = 0
            for i in range(length-1, -1, -1):
                if state[i] == '+':
                    inc += 1
                else:
                    break
            # print("flip all:", length, inc, state[:length-inc])
            return flip_count(state[:length-inc]) + 1
        else:  # last pancake is '+'
            length = len(state)
            inc = 0
            for i in range(length-1, -1, -1):
                if state[i] == '+':
                    inc += 1
                else:
                    break
            for i in range(length-inc):
                if state[i] == '-':
                    state[i] = '+'
                else:
                    state[i] = '-'
            # print(inc, state[:-inc])
            return flip_count(state[:-inc]) + 1

# state = []
# #signs = '+++-'
# #signs = '-+++--++--'
# signs = '+--+-++-++'
# for sign in signs:
#     state.append(sign)
# print(state)
# print(flip_count(state))

infile = open("B-large.in", 'r')
# infile = open("b1.in", 'r')
outfile = open("B-large.out", 'w')
T = int(infile.readline())
signs = infile.readlines()
k = 1
for sign in signs:
    states = []
    sign = sign.strip()
    # print(sign)
    for x in range(len(sign)):
        states.append(sign[x])
    # print(states)
    outfile.write("Case #" + str(k) + ": " + str(flip_count(states)) + '\n')
    k += 1
infile.close()
outfile.close()
