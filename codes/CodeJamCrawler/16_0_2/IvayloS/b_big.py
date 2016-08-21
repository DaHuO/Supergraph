import sys

def solve(states, length):
    answer = 0
    while length > 0 and states[length - 1] == 1:
        length -= 1
    if length == 0:
        return 0
    prefix = 0
    while prefix < length and states[prefix] == 1:
        prefix += 1
    if prefix > 0:
        for i in range(prefix):
            states[i] = 1 - states[i]
        answer += 1
    for i in range(length):
        states[i] = 1 - states[i]
    answer += 1
    return answer + solve(states, length)

tests = int(sys.stdin.readline())

for testnum in range(1, tests + 1):
    input = sys.stdin.readline().strip()
    states = list(map(lambda t: 1 if t == "+" else 0, input))
    moves = solve(states, len(states))
    print("Case #{}: {}".format(testnum, moves))
