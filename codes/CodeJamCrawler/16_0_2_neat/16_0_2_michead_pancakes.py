from sys import argv

IN_FILE = argv[1]
OUT_FILE = 'out.txt'

num_tests = 0
stacks = []
num_moves = []

with open (IN_FILE, 'r') as r:
    for i, line in enumerate(r):
        if not i:
            num_tests = int(line.rstrip())
        else:
            stacks.append(line.rstrip())

def get_min_num_moves (stack, num_moves):

    index_minus = stack.find('-')
    index_plus = stack.find('+')

    if  index_minus != -1 and index_minus < index_plus:
        index = stack[:index_plus].rfind('-') + 1
        s1_ = stack[:index][::-1]
        s2 = stack[index:]
    else:
        index = stack.rfind('-')
        if index == - 1:
            return num_moves
        else:
            index += 1
            index2 = stack[:index].rfind('+')
            if index2 == -1:
                s1_ = stack[:index][::-1]
                s2 = stack[index:]
            else:
                index2 += 1
                s1_ = stack[:index2][::-1]
                s2 = stack[index2:]
    s1 = ''
    for c in s1_:
        if c == '-':
            s1 += '+'
        else:
            s1 += '-'
    return get_min_num_moves(s1 + s2, num_moves + 1)


for stack in stacks:
    num_moves.append(get_min_num_moves(stack, 0))

with open (OUT_FILE, 'w') as w:
    for i, num_moves in enumerate(num_moves):
        w.write('Case #' + str(i + 1) + ': ' + str(num_moves) + '\n')
