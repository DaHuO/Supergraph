def get_least_flips(state):
    if len(state) == 1:
        return 0 if state == '+' else 1
    flips_needed = 0
    for i in xrange(1, len(state), 1):
        if not state[i] == state[i-1]:
            flips_needed += 1
    flips_needed += 0 if state[-1] == '+' else 1
    return flips_needed

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        state = raw_input()
        flips_needed = min(get_least_flips(state), 1+ get_least_flips(state[::-1]))
        print "Case #{}: {}".format(i+1, flips_needed)