test_cases = input()

def print_result(t, result):
    print "Case #" + str(t + 1) + ": " + str(result)

def handle_case(t):
    moves = 0
    last = ''
    for ch in raw_input():
        if ch == '-':
            if last == '':
                moves += 1
            elif last == '+':
                moves += 2
            last = '-'
        elif ch == '+':
            last = '+'

    print_result(t, moves)


for t in range(0, test_cases):
    handle_case(t)


