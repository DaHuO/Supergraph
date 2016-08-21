import sys

def is_happy(x):
    return x == '+'

def is_blank(x):
    return x == '-'

def are_all_happy(S):
    return all(map(is_happy, S))

def are_all_blank(S):
    return all(map(is_blank, S))

def flip(x):
    return '+' if x == '-' else '-'

def find_first_blanks(S):
    low = -1
    high = -1
    for i in xrange(len(S)):
        if is_blank(S[i]):
            if low == -1:
                low = i
            high = i
        else:
            if low != -1:
                break
    return [low, high]

def execute_the_maneuver(S, i):
   return ''.join(map(flip, S[0:i])) + S[i:]

def get_minimum_maneuvers(S):
    times = 0
    while not are_all_happy(S):
        [low, high] = find_first_blanks(S)
        if low == 0:
            S = execute_the_maneuver(S, high + 1)     
            times += 1
        else:
            S = execute_the_maneuver(S, low)
            S = execute_the_maneuver(S, high + 1)
            times += 2
    return times

T = int(sys.stdin.readline())
for t in xrange(T):
    S = sys.stdin.readline()
    print 'Case #' + str(t+1) + ': ' + str(get_minimum_maneuvers(S.strip()))

