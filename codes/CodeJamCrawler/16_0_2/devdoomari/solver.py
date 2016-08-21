import sys

input_lines = sys.stdin.read().split('\n')
# input_lines = open('./A-small-practice.in', 'r').read().split('\n')
# input_lines = open('./test_input.txt', 'r').read().split('\n')

# work back-ward: start from +++++++, flip to get to the 'initial state'!

def flip(state, n):
    flipped_bits = []
    for i in range(n-1, -1, -1):
        flipped_bits.append(not state[i])
    return flipped_bits + state[n:]

def get_reversed_state(state):
    copy = state[:]
    return copy.reverse()

def get_full_state(state):
    return list(map(lambda n: True, state))

def solve(state):
    moving_state = get_full_state(state)
    # reversed_state = get_reversed_state(state)
    flip_count = 0
    for i in range(len(state)-1, -1, -1):
        if moving_state[i] != state[i]:
            moving_state = flip(moving_state, i)
            flip_count = flip_count + 1
    return flip_count

def translate_to_bool(plus_minus_str):
    if plus_minus_str == "+":
        return True
    return False

for i in range(1, len(input_lines)):
    input_line = input_lines[i]
    if len(input_line) == 0:
        continue
    state = list(map(translate_to_bool, list(input_line)))
    print("Case #{i}: {result}".format(
        i=i, result=solve(state)
    ))
